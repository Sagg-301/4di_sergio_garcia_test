from .Command import Command

class ExampleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self):
        pass

    def execute(self):
        return 0