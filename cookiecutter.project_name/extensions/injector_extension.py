from flask_injector import FlaskInjector
from injector import singleton, Binder

from core.domain.{{cookiecutter.api_2_for_name}}.repository.{{cookiecutter.api_2_for_name}}_repository import {{cookiecutter.api_2_for_name}}Repository
from core.domain.{{cookiecutter.api_2_for_name}}.use_case.get_user_{{cookiecutter.api_2_for_name}} import GetUser{{cookiecutter.api_2_for_name}}UseCase
from infra.sql.{{cookiecutter.api_2_for_name}}.repository.sql_{{cookiecutter.api_2_for_name}}_repository import Sql{{cookiecutter.api_2_for_name}}Repository
# from infra.mock.repository import Mock{{cookiecutter.api_2_for_name}}Repository


def configure_binding(binder: Binder) -> Binder:
    binder.bind(GetUser{{cookiecutter.api_2_for_name}}UseCase, to=GetUser{{cookiecutter.api_2_for_name}}UseCase, scope=singleton)
    # binder.bind({{cookiecutter.api_2_for_name}}Repository, to=Mock{{cookiecutter.api_2_for_name}}Repository, scope=singleton)
    binder.bind({{cookiecutter.api_2_for_name}}Repository, to=Sql{{cookiecutter.api_2_for_name}}Repository, scope=singleton)
    return binder


def register_dependency_injection(app):
    FlaskInjector(app=app, modules=[configure_binding])
