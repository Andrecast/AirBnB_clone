#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = __class__.__name__
        my_dict["created_at"] = datetime.isoformat(self.created_at)
        my_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return my_dict

