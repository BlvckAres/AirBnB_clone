#!/usr/bin/python3
"""The following script is for the BaseModel class."""

import datetime
from uuid import uuid4
import models


class BaseModel:

    """ Represents the BaseModel class for the project."""

    def __init__(self, *args, **kwargs):
        """Initializes a the BaseModel

        Args:
            - *args: the entered args.
            - **kwargs (dict): key/value of the args
        """
        tmeform = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0 and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tmeform)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """Returns string representation of the class name, id, dict"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

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