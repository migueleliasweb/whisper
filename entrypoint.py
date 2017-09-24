#!/usr/bin/env python3
from os import getenv, execvpe, environ
# from whisper.webserver import app
#
# if __name__ == "__main__":
#     app.run()

uwsgi_args = [
    "uwsgi",
    "--master",
    "--threads", getenv('UWSGI_THREADS', '4'),
    "--processes", getenv('UWSGI_PROCESSES', '2'),
    "--http", getenv('UWSGI_BIND', '0.0.0.0:8080'),
    "--module", "whisper.webserver",
    "--callable", "app"
]

execvpe('uwsgi', uwsgi_args, environ)
