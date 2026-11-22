import pytest
from flask import g
from flask import session

from flaskr.db import get_db


def test_register(client, app):
    # test that viewing the page renders without template errors
    assert client.get("/auth/register").status_code == 200

    # test that successful registration redirects to the login page
    response = client.post("/auth/register", data={"username": "a", "password": "abcdefgh"})
    assert response.headers["Location"] == "/auth/login"

    # test that the user was inserted into the database
    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM user WHERE username = 'a'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("test", "abcdefgh", b"already registered"),
    ),
)
def test_register_validate_input(client, username, password, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password}
    )
    assert message in response.data


def test_register_password_too_short(client, app):
    # Intento registrar un usuario con una contraseña de 7 caracteres.
    response = client.post(
        "/auth/register",
        data={"username": "usuario7", "password": "abcdefg"},
    )

    # Compruebo que el programa muestra el mensaje de error.
    assert b"Password must be at least 8 characters." in response.data

    # Compruebo en la base de datos que el usuario no se ha creado.
    with app.app_context():
        user = get_db().execute(
            "SELECT id FROM user WHERE username = ?", ("usuario7",)
        ).fetchone()
        assert user is None


def test_register_password_8_characters(client, app):
    # Pruebo una contraseña que tiene exactamente 8 caracteres.
    response = client.post(
        "/auth/register",
        data={"username": "usuario8", "password": "abcdefgh"},
    )

    # Compruebo que el registro se acepta y me lleva al login.
    assert response.headers["Location"] == "/auth/login"

    # Compruebo que el usuario se ha guardado en la base de datos.
    with app.app_context():
        user = get_db().execute(
            "SELECT id FROM user WHERE username = ?", ("usuario8",)
        ).fetchone()
        assert user is not None


def test_register_password_9_characters(client, app):
    # Pruebo una contraseña de 9 caracteres, que supera el mínimo.
    response = client.post(
        "/auth/register",
        data={"username": "usuario9", "password": "abcdefghi"},
    )

    # Compruebo que el registro se acepta y redirige al login.
    assert response.headers["Location"] == "/auth/login"

    # Compruebo que el nuevo usuario existe en la base de datos.
    with app.app_context():
        user = get_db().execute(
            "SELECT id FROM user WHERE username = ?", ("usuario9",)
        ).fetchone()
        assert user is not None

def test_login(client, auth):
    # test that viewing the page renders without template errors
    assert client.get("/auth/login").status_code == 200

    # test that successful login redirects to the index page
    response = auth.login()
    assert response.headers["Location"] == "/"

    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["username"] == "test"


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "test", b"Incorrect username."), ("test", "a", b"Incorrect password.")),
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session
