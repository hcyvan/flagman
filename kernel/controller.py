from flask import request


class Controller:
    def __init__(self):
        self.request = request

    def args(self, key, default=None):
        return self.request.args.get(key, default)

    def json(self, key, default=None):
        return self.request.json.get(key, default)
