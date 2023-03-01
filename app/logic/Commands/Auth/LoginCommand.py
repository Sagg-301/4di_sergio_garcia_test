from ....models import UserModel
from ..Command import Command
from ....persistence.UserDAO import UserDAO
from ....common.Exceptions import *
import bcrypt


class LoginCommand(Command):
    """
    Login command
    """

    def __init__(self, payload):
        self._payload = payload

    def execute(self) -> UserModel:
        dao = UserDAO()

        user = dao.find_by_user(self._payload['user'])
        if user and not user.deleted:
            if bcrypt.checkpw(bytes(self._payload["password"], 'utf-8'), bytes(user.password, 'utf-8')):
                return user
            else:
                raise InvalidCredentialsException()
        else:
            raise InvalidCredentialsException(
                {"user": ["User does not exists or is deactivated"]})
