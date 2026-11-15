<div align="center"><img src="https://raw.githubusercontent.com/pallets/flask/refs/heads/stable/docs/_static/flask-name.svg" alt="" height="150"></div>

# Flask

Flask is a lightweight [WSGI] web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around [Werkzeug]
and [Jinja], and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/

## A Simple Example

```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Donate

The Pallets organization develops and supports Flask and the libraries
it uses. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/



## Diagramas de secuencia - Flaskr

En esta práctica he hecho cuatro diagramas de secuencia para mostrar cómo funciona el login de Flaskr y qué pasa cuando hay algún error.

- [Login correcto](diagrams/login_correcto.png): El usuario pone sus datos correctamente y consigue iniciar sesión.
- [Usuario incorrecto](diagrams/login_usuario_incorrecto.drawio.png): El usuario no existe y Flaskr muestra un error.
- [Contraseña incorrecta](diagrams/login_contrasena_incorrecta.drawio.png): El usuario existe, pero la contraseña no es correcta.
- [Servidor no disponible](diagrams/login_servidor_no_disponible.png): El servidor está apagado y el navegador no puede abrir Flaskr.
