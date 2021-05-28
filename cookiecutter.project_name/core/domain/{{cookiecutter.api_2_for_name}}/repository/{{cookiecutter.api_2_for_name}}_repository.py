from abc import ABC, abstractmethod
from typing import List

from core.domain.{{cookiecutter.api_2_for_name}}.entity.user import User, UserBasic{{cookiecutter.api_2_for_name}}, UserExtra{{cookiecutter.api_2_for_name}}


class {{cookiecutter.api_2_for_name}}Repository(ABC):

    @abstractmethod
    def get_user(self, user_type: str, user_id: int) -> User:
        return NotImplemented

    @abstractmethod
    def create_user(self, user: User) -> None:
        return NotImplemented

    @abstractmethod
    def update_user_basic(self, user_type: str, user_id: int, basic_{{cookiecutter.api_2_for_name}}: UserBasic{{cookiecutter.api_2_for_name}}) -> None:
        return NotImplemented

    @abstractmethod
    def update_user_extra(self, user_type: str, user_id: int, extra_{{cookiecutter.api_2_for_name}}s: List[UserExtra{{cookiecutter.api_2_for_name}}]) -> None:
        return NotImplemented
