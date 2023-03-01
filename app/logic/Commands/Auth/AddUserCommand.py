from ..Command import Command
from ....persistence.UserDAO import UserDAO


class AddUserCommand(Command):
    """
    Add User command
    """

    def __init__(self, payload):
        self._payload = payload

    def execute(self) -> int:
        dao = UserDAO()

        response = dao.add(self._payload)
        return response
