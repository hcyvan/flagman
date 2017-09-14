from http import HTTPStatus
from flask import request, jsonify


class Controller:
    def __init__(self):
        self.request = request

    def args(self, key, default=None):
        return self.request.args.get(key, default)

    def json(self, key, default=None):
        return self.request.json.get(key, default)

    @staticmethod
    def echo(code=0, data=None, message='', status=None):
        result = {'code': code}
        if data:
            result['data'] = data
        if message:
            result['msg'] = message
        if not status:
            status = HTTPStatus.OK
        return jsonify(result), status
