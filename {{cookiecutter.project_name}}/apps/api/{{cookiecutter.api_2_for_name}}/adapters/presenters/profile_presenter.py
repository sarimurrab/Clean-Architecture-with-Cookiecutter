from apps.shared.global_exception import NotFoundError

from core.domain.{{cookiecutter.api_2_for_name}}.use_case.get_user_{{cookiecutter.api_2_for_name}} import GetUser{{cookiecutter.api_2_for_name}}Response
from core.kernel.exception import BaseNotFoundException
from core.kernel.port import JsonContentResult
from core.kernel.use_case import UseCaseOutputPort


class GetUser{{cookiecutter.api_2_for_name}}Presenter(UseCaseOutputPort[GetUser{{cookiecutter.api_2_for_name}}Response], JsonContentResult):

    def handle(self, response: GetUser{{cookiecutter.api_2_for_name}}Response) -> None:
        if not response.is_succeeded:
            if isinstance(response.error, BaseNotFoundException):
                raise NotFoundError(response.error.message)
        self.content_result = response
