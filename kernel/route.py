from functools import update_wrapper
from .app import app

import stringcase


def auto_import(func):
    def wrapper(path, controller):
        if isinstance(controller, str):
            try:
                _class_name, _method_name = controller.split('@')
            except:
                raise Exception('Controller string should be like calss@method')
            # todo: Read __import__ docs
            _module = __import__('controllers.' + stringcase.snakecase(_class_name))
            _sub_module = getattr(_module, stringcase.snakecase(_class_name))
            _class = getattr(_sub_module, _class_name)
            controller = getattr(_class(), _method_name)
        return func(path, controller)

    return update_wrapper(wrapper, func)


class Route:
    @staticmethod
    @auto_import
    def get(path, controller):
        app.add_url_rule(path, view_func=controller, methods=['GET'])

    @staticmethod
    @auto_import
    def post(path, controller):
        app.add_url_rule(path, view_func=controller, methods=['POST'])

    @staticmethod
    @auto_import
    def delete(path, controller):
        app.add_url_rule(path, view_func=controller, methods=['DELETE'])

    @staticmethod
    @auto_import
    def patch(path, controller):
        app.add_url_rule(path, view_func=controller, methods=['PATCH'])

    @staticmethod
    @auto_import
    def put(path, controller):
        app.add_url_rule(path, view_func=controller, methods=['PUT'])
