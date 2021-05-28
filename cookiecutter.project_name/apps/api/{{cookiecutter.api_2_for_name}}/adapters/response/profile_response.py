from flask_restplus import fields

from apps.api.{{cookiecutter.api_2_for_name}}.controllers import member_api

entity = member_api.model('Entity', {
    'id': fields.Integer
})

basic_{{cookiecutter.api_2_for_name}} = member_api.model('Basic{{cookiecutter.api_2_for_name}}', {
    'real_name': fields.String,
    'gender': fields.String,
    # 'birthday': fields.String
})

extra_{{cookiecutter.api_2_for_name}} = member_api.model('Extra{{cookiecutter.api_2_for_name}}', {
    '{{cookiecutter.api_2_for_name}}_category': fields.String,
    '*': fields.Wildcard(fields.String)
})

user_{{cookiecutter.api_2_for_name}} = member_api.clone('User{{cookiecutter.api_2_for_name}}', entity, {
    'user_type': fields.String,
    'user_name': fields.String,
    'user_status': fields.String,
})

member_{{cookiecutter.api_2_for_name}} = member_api.clone('Member{{cookiecutter.api_2_for_name}}', user_{{cookiecutter.api_2_for_name}}, {
    'basic_{{cookiecutter.api_2_for_name}}': fields.Nested(basic_{{cookiecutter.api_2_for_name}}),
    'extra_{{cookiecutter.api_2_for_name}}': fields.List(fields.Nested(extra_{{cookiecutter.api_2_for_name}}))
})
