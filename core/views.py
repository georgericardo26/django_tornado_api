import datetime
import json
import asyncio
import tornado.web as web
from tornado.httpclient import HTTPResponse
from tornado.gen import coroutine
from tornado import httpclient


class BaseView(web.RequestHandler):

    def prepare(self):
        self.form_data = {
            key: [val.decode('utf8') for val in val_list]
            for key, val_list in self.request.arguments.items()
        }

    def set_default_headers(self):
        """Set the default response header to be JSON."""
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def send_response(self, data, status=200):
        """Construct and send a JSON response with appropriate status code."""
        self.set_status(status)

        # HTTPResponse(request=self.request, code=200, buffer=json.dumps(data))
        self.write(json.dumps(data))


class UserView(BaseView):
    SUPPORTED_METHODS = ["GET"]

    async def get(self):
        self.send_response({"user": "George Ricardo"})
