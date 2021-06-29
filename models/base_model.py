#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        This class defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initial method that store the attributes
        args:
            id: The UUID to identify the instances
            created_at: to assign the datetime to an instance
            updated_at: to update the datetime of an instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key in ('created_at', 'updated_at'):
                    date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Human reading
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.isoformat(self.created_at)
        my_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return my_dict
