import attr
from datetime import date

from core.kernel.entity import ValueObject


@attr.s(auto_attribs=True)
class UserBasic{{cookiecutter.api_2_for_name}}(ValueObject):
    """ User Basic {{cookiecutter.api_2_for_name}} """
    real_name: str = None
    gender: str = None
    birthday: str = None


@attr.s(auto_attribs=True)
class UserExtra{{cookiecutter.api_2_for_name}}(ValueObject):
    """ Base User Extra {{cookiecutter.api_2_for_name}} """
    {{cookiecutter.api_2_for_name}}_category: str = None


@attr.s(auto_attribs=True)
class EducationExtra{{cookiecutter.api_2_for_name}}(UserExtra{{cookiecutter.api_2_for_name}}):
    """ Education Extra {{cookiecutter.api_2_for_name}} """
    {{cookiecutter.api_2_for_name}}_category: str = attr.ib(default="education", init=False)
    school: str = None
    department: str = None


@attr.s(auto_attribs=True)
class CareerExtra{{cookiecutter.api_2_for_name}}(UserExtra{{cookiecutter.api_2_for_name}}):
    """ Career Extra {{cookiecutter.api_2_for_name}} """
    {{cookiecutter.api_2_for_name}}_category: str = attr.ib(default="career", init=False)
    career: str = None
    job_title: str = None
