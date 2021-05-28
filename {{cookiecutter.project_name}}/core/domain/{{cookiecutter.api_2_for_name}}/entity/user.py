import attr
from typing import List

from core.kernel.entity import Entity
from .{{cookiecutter.api_2_for_name}} import UserBasic{{cookiecutter.api_2_for_name}}, UserExtra{{cookiecutter.api_2_for_name}}


@attr.s(auto_attribs=True)
class User(Entity):
    """ Base User Entity """
    user_type: str = None
    user_name: str = None
    user_status: str = "enabled"
    basic_{{cookiecutter.api_2_for_name}}: UserBasic{{cookiecutter.api_2_for_name}} = None
    extra_{{cookiecutter.api_2_for_name}}: List[UserExtra{{cookiecutter.api_2_for_name}}] = []


@attr.s(auto_attribs=True)
class Member(User):
    """ Member Entity Extends User """
    user_type: str = attr.ib(default="member", init=False)


@attr.s(auto_attribs=True)
class Newcomer(User):
    """ Newcomer Entity Extends User """
    user_type: str = attr.ib(default="newcomer", init=False)
