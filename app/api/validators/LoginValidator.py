from cerberus import Validator
from ...common.Exceptions import *
from cerberus import Validator


class LoginValidator():
    """
    Validation for User object
    """

    validator = Validator({
        'password': {"type": "string", 'empty': False},
        'user': {"type": "string", 'empty': False},
    })

    def __init__(self, data):
        self.data = data

    def validate(self):
        """
        Validate fields
        """
        if not self.validator.validate(self.data):
            raise ValidationException(
                self.validator.errors)
