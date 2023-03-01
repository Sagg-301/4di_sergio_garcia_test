from .BaseModel import BaseModel
from app import db


class PublicationModel(BaseModel):

    __tablename__ = 'Publication'

    title = db.Column(db.String(128),  nullable=False, unique=True)
    description = db.Column(db.String(800),  nullable=False)
    priority = db.Column(db.Integer,  nullable=False)
    status = db.Column(db.Boolean,  nullable=False, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    def __init__(self, title: str, description: str, priority: int, status: bool, user_id: int):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return '<Publication %r>' % (self.title)

    def get_id(self):
        return self.id

    def serialize(self):
        """
        Return as dict
        """

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "user_id": self.user_id,
            "date_created": self.date_created,
            "date_modified": self.date_modified,
        }
