from typing import Union
from ..Command import Command
from ....persistence.UserDAO import UserDAO
from ....models import UserModel


class DeactivateUserCommand(Command):
    """
    Add User command
    """

    def __init__(self, payload):
        self._payload = payload

    def execute(self) -> Union[UserModel, None]:
        dao = UserDAO()

        response = dao.delete(self._payload)
        return response
