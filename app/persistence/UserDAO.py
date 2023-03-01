from __future__ import annotations
from typing import Union
from .DAO import DAO
from ..models.UserModel import UserModel
import bcrypt
import traceback
from app import db


class UserDAO(DAO):
    """
    Data Access Object Abstract Class.
    """

    
    def add(self, data) -> int:
        """
        Adds a new record
        """
        pass

    def get(self):
        """
        Gets alll records from the Database
        """
        pass

    def find(self, id) -> UserModel:
        """
        Find a single record from the Database by id
        """
        try:
            user = UserModel.query.filter_by(id=id).first()

            return user
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def find_by_user(self, user) -> UserModel:
        """
        Find a single record from the Database by id
        """
        try:
            user = UserModel.query.filter_by(user=user).first()

            return user
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def update(self, data) -> Union[UserModel, None]:
        """
        Updates a Record on the Database 
        """
        pass

    def delete(self, id) -> bool:
        """

        Deletes a record on the Database
        """
        pass
