import os

from django.core.wsgi import get_wsgi_application
from tornado.options import parse_command_line
from tornado.web import Application, FallbackHandler
from tornado.wsgi import WSGIContainer


class ApplicationBase(Application):

    os.environ['DJANGO_SETTINGS_MODULE'] = 'ebanking.settings'  # TODO: edit this
    parse_command_line()
    wsgi_app = get_wsgi_application()
    container = WSGIContainer(wsgi_app)

    _routes = [
        ('.*', FallbackHandler, dict(fallback=container))
    ]

    def __init__(self, routes: list):
        self._routes = routes + self._routes
        settings = {"debug": True}
        super(ApplicationBase, self).__init__(self._routes, **settings)