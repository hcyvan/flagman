from .app import app

import stringcase


class Route:
    @staticmethod
    def get(path, controller):
        if isinstance(controller, str):
            try:
                _class_name, _method_name = controller.split('@')
            except:
                raise Exception('Controller string should be like calss@method')
            # todo: Read __import__ docs
            _module = __import__('controllers.'+stringcase.snakecase(_class_name))
            _sub_module = getattr(_module, stringcase.snakecase(_class_name))
            _class = getattr(_sub_module, _class_name)
            controller = getattr(_class(), _method_name)
        app.add_url_rule(path, view_func=controller)
