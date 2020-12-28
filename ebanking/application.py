import os

from django.core.wsgi import get_wsgi_application
from tornado.options import parse_command_line
from tornado.web import Application, FallbackHandler
from tornado.wsgi import WSGIContainer
from tornado_swagger.setup import setup_swagger


class ApplicationBase(Application):

    os.environ['DJANGO_SETTINGS_MODULE'] = 'ebanking.settings'  # TODO: edit this
    parse_command_line()
    wsgi_app = get_wsgi_application()
    container = WSGIContainer(wsgi_app)

    _routes = [
        ('.*', FallbackHandler, dict(fallback=container))
    ]

    def __init__(self, routes: list):
        # self._routes = routes + self._routes
        settings = {"debug": True}
        setup_swagger(
            routes,
            swagger_url="/doc",
            description="",
            api_version="1.0.0",
            title="eBanking API",
            contact=dict(name="George Ricardo", email="georgericardo26@gmail.com", url="https://www.cookbooknerd.com"),
        )

        self._routes = routes + self._routes

        super(ApplicationBase, self).__init__(self._routes, **settings)
