# import os
#
# import tornado.httpserver
# import tornado.ioloop
# import tornado.web
# import tornado.wsgi
# from django.core.wsgi import get_wsgi_application
# from tornado.wsgi import WSGIContainer
#
# from tornado.options import options, define, parse_command_line
#
# define('port', type=int, default=8080)
#
# class HelloHandler(tornado.web.RequestHandler):
#   def get(self):
#     self.write('Hello from tornado')
#
# def main():
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'ebanking.settings'  # TODO: edit this
#
#     parse_command_line()
#
#     wsgi_app = get_wsgi_application()
#     container = WSGIContainer(wsgi_app)
#     tornado_app = tornado.web.Application(
#         [
#             ('/hello-tornado', HelloHandler),
#             ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
#         ])
#     # tornado_app = ApplicationBase()
#
#     server = tornado.httpserver.HTTPServer(tornado_app)
#     server.listen(options.port)
#     print('Listening on http://localhost:%i' % options.port)
#     tornado.ioloop.IOLoop.instance().start()
#
#
# if __name__ == '__main__':
#     main()


import sys
import os

from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

from ebanking.urls import URL_PATTERNS

define('port', type=int, default=8080)


def main():

    server = tornado.httpserver.HTTPServer(URL_PATTERNS)
    server.listen(options.port)

    print('Listening on http://localhost:%i' % options.port)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
