#!/usr/bin/python3
"""This module serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
from os import path


class FileStorage:
    """Class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Will return the objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj.to_dict()

    def save(self):
        """To serializes
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as write_file:
            json.dump(FileStorage.__objects, write_file)

    def reload(self):
        """To deserializes
        """
        try:
            if path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r") as write_file:
                    json.load(write_file)
        except:
            pass
