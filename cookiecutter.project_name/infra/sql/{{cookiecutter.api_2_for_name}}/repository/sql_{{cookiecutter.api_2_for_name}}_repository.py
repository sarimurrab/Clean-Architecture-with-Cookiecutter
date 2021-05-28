from typing import List

from core.domain.{{cookiecutter.api_2_for_name}}.entity.{{cookiecutter.api_2_for_name}} import (
    UserBasic{{cookiecutter.api_2_for_name}}, EducationExtra{{cookiecutter.api_2_for_name}}, CareerExtra{{cookiecutter.api_2_for_name}}, UserExtra{{cookiecutter.api_2_for_name}}
)
from core.domain.{{cookiecutter.api_2_for_name}}.entity.user import User, Member, Newcomer
from core.domain.{{cookiecutter.api_2_for_name}}.exception import UserNotFound
from core.domain.{{cookiecutter.api_2_for_name}}.repository.{{cookiecutter.api_2_for_name}}_repository import {{cookiecutter.api_2_for_name}}Repository


class Sql{{cookiecutter.api_2_for_name}}Repository({{cookiecutter.api_2_for_name}}Repository):
    _users: List[User] = []

    def __init__(self):
        education_{{cookiecutter.api_2_for_name}} = EducationExtra{{cookiecutter.api_2_for_name}}(school="College", department="CSE")
        career_{{cookiecutter.api_2_for_name}} = CareerExtra{{cookiecutter.api_2_for_name}}(career="Developer", job_title="Python developer")
        member = Member(
            id=111,
            user_name="Sarim",
            user_status="enabled",
            basic_{{cookiecutter.api_2_for_name}}=UserBasic{{cookiecutter.api_2_for_name}}(real_name="Hello Sarim", gender="Male", birthday=""),
            extra_{{cookiecutter.api_2_for_name}}=[education_{{cookiecutter.api_2_for_name}}, career_{{cookiecutter.api_2_for_name}}]
        )
        newcomer = Newcomer(
            id=112,
            user_name="Raj",
            user_status="enabled",
            basic_{{cookiecutter.api_2_for_name}}=UserBasic{{cookiecutter.api_2_for_name}}(real_name="Hello Raj", gender="Male", birthday=""),
            extra_{{cookiecutter.api_2_for_name}}=[career_{{cookiecutter.api_2_for_name}}]
        )
        self._users.append(member)
        self._users.append(newcomer)

    def get_user(self, user_type: str, user_id: int) -> User:
        user = next((x for x in self._users if x.id ==
                     user_id and x.user_type == user_type), None)
        return user

    def create_user(self, user: User) -> None:
        self._users.append(user)

    def update_user_basic(self, user_type: str, user_id: int, basic_{{cookiecutter.api_2_for_name}}: UserBasic{{cookiecutter.api_2_for_name}}) -> None:
        user = next((x for x in self._users if x.id ==
                     user_id and x.user_type == user_type), None)
        if user:
            user.basic_{{cookiecutter.api_2_for_name}} = basic_{{cookiecutter.api_2_for_name}}
        else:
            raise UserNotFound()

    def update_user_extra(self, user_type: str, user_id: int, extra_{{cookiecutter.api_2_for_name}}s: List[UserExtra{{cookiecutter.api_2_for_name}}]) -> None:
        user = next((x for x in self._users if x.id ==
                     user_id and x.user_type == user_type), None)
        if user:
            user.extra_{{cookiecutter.api_2_for_name}} = extra_{{cookiecutter.api_2_for_name}}s
        else:
            raise UserNotFound()
