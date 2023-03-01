from .BaseModel import BaseModel
from app import db


class UserModel(BaseModel):

    __tablename__ = 'User'

    user = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    full_name = db.Column(db.String(192),  nullable=False)
    deleted = db.Column(db.Boolean,  nullable=False, default=False)

    def __init__(self, user: str, password: str, full_name: str):

        self.user = user
        self.full_name = full_name
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def serialize(self):
        """
        Return as dict
        """

        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.user,
            "date_created": self.date_created,
            "date_modified": self.date_modified,
        }
