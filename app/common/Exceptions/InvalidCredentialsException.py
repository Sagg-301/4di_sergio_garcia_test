class InvalidCredentialsException(Exception):
    """Exception raised for validations.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message={'credentials': ["Wrong email or password"]}):
        self.message = message
        super().__init__(self.message)
