#!/usr/bin/python3
"""Base class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
        This class defines all common attributes/methods for other classes
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Initial method that store the attributes
        args:
            id: The UUID to identify the instances
            created_at: to assign the datetime to an instance
            updated_at: to update the datetime of an instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Human reading
        """
        return "[{}] ({}) {}".format(
            __class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = __class__.__name__
        my_dict["created_at"] = datetime.isoformat(self.created_at)
        my_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return my_dict
