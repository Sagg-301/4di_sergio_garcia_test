from app.common.Exceptions.InvalidCredentialsException import InvalidCredentialsException
from app.logic.Commands import *
import pytest
from flask_login import current_user, login_required, logout_user, login_user

class TestLogin:


    def test_login(self):
        command = LoginCommand({
            "user": "admin@test.com",
            "password": "12345678"
        })

        user = command.execute()

        assert user.full_name == "John Smith"

    def test_wrong_credentials_login(self):
        command = LoginCommand({
            "user": "test@gmail.com",
            "password": "123456782"
        })

        with pytest.raises(InvalidCredentialsException):
            command.execute()