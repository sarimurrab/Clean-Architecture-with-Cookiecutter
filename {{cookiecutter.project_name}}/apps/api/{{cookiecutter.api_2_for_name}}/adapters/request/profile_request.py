from flask_restplus import fields

from apps.api.{{cookiecutter.api_2_for_name}}.controllers import member_api

member_id_request = member_api.model('MemberIdRequest', {
    'id': fields.Integer
})
