from flask import Blueprint
from flask_restplus import Api
from werkzeug.exceptions import HTTPException

from .{{cookiecutter.api_for_name}}.controllers.security import api as security_api

blueprint = Blueprint('{{cookiecutter.api_for_name}}_api',
                      __name__, url_prefix='/{{cookiecutter.api_for_name}}/v1')

api = Api(blueprint,
          doc='/doc/',
          title='Resource API - {{cookiecutter.api_for_name}}',
          version='1.0',
          description='A description'
          )

api.add_namespace(security_api)


@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """ Handle BluePrint JSON Error Response """
    response = {
        'error': error.__class__.__name__,
        'message': error.description,
    }
    return response, error.code
