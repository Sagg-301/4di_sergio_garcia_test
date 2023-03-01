from __future__ import annotations
from typing import Union
from .DAO import DAO
from ..models.PublicationModel import PublicationModel
import traceback
from app import db
from sqlalchemy import func


class PublicationDAO(DAO):
    """
    Data Access Object Abstract Class.
    """

    def add(self, data) -> int:
        try:
            publication = PublicationModel(
                data['title'], data['description'], data['priority'], True, data['user_id'])
            db.session.add(publication)
            db.session.commit()

            return publication.id
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def get(self):
        """
        Gets all records from the Database
        """
        pass

    def get_by_user(self, query):
        """
        Gets all records from the Database
        """
        try:
            publications = PublicationModel.query.order_by(PublicationModel.date_created.desc()).filter_by(
                user_id=query['user_id']).paginate(page=int(query['page']), per_page=int(query['per_page']))
            return publications
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def find(self, id) -> Union[PublicationModel, None]:
        """
        Find a single record from the Database by id
        """
        try:
            publication = PublicationModel.query.filter_by(id=id).first()

            return publication
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def find_by_title(self, title) -> Union[PublicationModel, None]:
        """
        Find a single record from the Database by id
        """
        try:
            publication = PublicationModel.query.filter(
                func.lower(PublicationModel.title) == func.lower(title)).first()

            return publication
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def update(self, data) -> Union[PublicationModel, None]:
        """
        Updates a Record on the Database 
        """
        try:
            publication = PublicationModel.query.filter_by(
                id=data['id'], user_id=data['user_id']).first()
            if publication:
                publication.title = data['title']
                publication.description = data['description']
                publication.priority = data['priority']
                publication.status = data['status'] if 'status' in data.keys(
                ) else publication.status

                db.session.commit()

            return publication
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def delete(self, id) -> bool:
        """

        Deletes a record on the Database
        """
        try:
            publication = PublicationModel.query.filter_by(id=id).first()
            if publication:
                db.session.delete(publication)
                db.session.commit()

                return True

            return False
        except Exception as ex:
            traceback.print_exc()
            raise ex
