from apps.api.{{cookiecutter.api_for_name}}_v1 import blueprint as {{cookiecutter.api_for_name}}_api
from apps.api.{{cookiecutter.api_2_for_name}}_v1 import blueprint as {{cookiecutter.api_2_for_name}}_api


def register_routes(app):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint({{cookiecutter.api_for_name}}_api)
    app.register_blueprint({{cookiecutter.api_2_for_name}}_api)
