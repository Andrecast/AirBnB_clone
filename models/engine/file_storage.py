#!/usr/bin/python3
"""This module serializes instances to a JSON file
and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json
from os import path


class FileStorage:
    """Class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    dic_class = {"BaseModel": BaseModel}

    def all(self):
        """Will return the objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """To serializes
        """
        _dict = {}
        for key, value in FileStorage.__objects.items():
            _dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as write_file:
            json.dump(_dict, write_file)

    def reload(self):
        """To deserializes
        """
        try:
            with open(FileStorage.__file_path, "r") as write_file:
                data = json.load(write_file)
                FileStorage.__objects = {}
                for key, value in data.items():
                    FileStorage.__objects[key] = FileStorage.dic_class[value['__class__']](**value)
        except:
            return
