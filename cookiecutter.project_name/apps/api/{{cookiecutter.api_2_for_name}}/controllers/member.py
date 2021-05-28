from flask_restplus import Resource
from injector import inject

from apps.api.{{cookiecutter.api_2_for_name}}.adapters.presenters.{{cookiecutter.api_2_for_name}}_presenter import GetUser{{cookiecutter.api_2_for_name}}Presenter
from apps.api.{{cookiecutter.api_2_for_name}}.adapters.response.{{cookiecutter.api_2_for_name}}_response import member_{{cookiecutter.api_2_for_name}}
from apps.api.{{cookiecutter.api_2_for_name}}.controllers import member_api as api
from apps.shared.global_exception import CustomError, BadRequestError, NotFoundError
from core.domain.{{cookiecutter.api_2_for_name}}.use_case.get_user_{{cookiecutter.api_2_for_name}} import GetUser{{cookiecutter.api_2_for_name}}UseCase, GetUser{{cookiecutter.api_2_for_name}}Request


@api.route('/')
class MemberList(Resource):
    @api.doc('Create Member')
    @api.response(400, 'Bad Request')
    def post(self):
        return ['create member']


@api.route('/<int:member_id>/')
class Member(Resource):

    @inject
    def __init__(self, uc_get_{{cookiecutter.api_2_for_name}}: GetUser{{cookiecutter.api_2_for_name}}UseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._uc_get_{{cookiecutter.api_2_for_name}} = uc_get_{{cookiecutter.api_2_for_name}}

    @api.doc('Get Member')
    @api.response(404, 'User Not Found')
    @api.marshal_with(member_{{cookiecutter.api_2_for_name}})
    def get(self, member_id: int):
        uc_request = GetUser{{cookiecutter.api_2_for_name}}Request(member_id, "member")
        presenter = GetUser{{cookiecutter.api_2_for_name}}Presenter()
        self._uc_get_{{cookiecutter.api_2_for_name}}.execute(uc_request, presenter)
        return presenter.content_result


@api.route('/<int:member_id>/basic')
class MemberBasic(Resource):
    @api.doc('Get Member Basic info')
    @api.response(404, 'User Not Found')
    def put(self, member_id: int):
        # return ['put member basic']
        raise CustomError('Bad key123')


@api.route('/<int:member_id>/extra')
class MemberExtra(Resource):
    @api.doc('Get Member Extra Info')
    @api.response(404, 'User Not Found')
    def put(self, member_id: int):
        # return ['put member extra']
        raise BadRequestError('wrong parameter abc')
