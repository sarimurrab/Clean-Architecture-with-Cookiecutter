import attr
from injector import inject

from core.domain.{{cookiecutter.api_2_for_name}}.exception import UserNotFound
from core.domain.{{cookiecutter.api_2_for_name}}.repository.{{cookiecutter.api_2_for_name}}_repository import {{cookiecutter.api_2_for_name}}Repository
from core.kernel.port import UseCaseRequest, UseCaseResponse, UseCaseOutputPort
from core.kernel.use_case import UseCase


@attr.s(auto_attribs=True)
class GetUser{{cookiecutter.api_2_for_name}}Request(UseCaseRequest):
    user_id: int = None
    user_type: str = None


@attr.s(auto_attribs=True)
class GetUser{{cookiecutter.api_2_for_name}}Response(UseCaseResponse):
    """ Extends UseCase Response """


class GetUser{{cookiecutter.api_2_for_name}}UseCase(UseCase):
    _{{cookiecutter.api_2_for_name}}_repo = None

    @inject
    def __init__(self, {{cookiecutter.api_2_for_name}}_repo: {{cookiecutter.api_2_for_name}}Repository):
        self._{{cookiecutter.api_2_for_name}}_repo = {{cookiecutter.api_2_for_name}}_repo

    def execute(self, uc_request: GetUser{{cookiecutter.api_2_for_name}}Request,
                uc_output_port: UseCaseOutputPort[GetUser{{cookiecutter.api_2_for_name}}Response]) -> None:
        response = GetUser{{cookiecutter.api_2_for_name}}Response()
        user = self._{{cookiecutter.api_2_for_name}}_repo.get_user(uc_request.user_type, uc_request.user_id)
        if not user:
            response.error = UserNotFound("This user does not exist")
        else:
            response.result = user
        uc_output_port.handle(response)


