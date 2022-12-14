#!/usr/bin/python3
"""The following script is for the BaseModel class."""

import datetime
from uuid import uuid4
import models


class BaseModel:

    """ Represents the BaseModel class for the project."""

    def __init__(self, *args, **kwargs):
        """Initializes a the BaseModel """

        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            return

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                self.__dict__[key] = datetime.fromisoformat(value)
            elif key != '__class__':
                self.__dict__[key] = value

    def __str__(self):
        """Returns string representation of the class name, id, dict"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at attribute with the current time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""

        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = self.__class__.__name__
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        return ret_dict
