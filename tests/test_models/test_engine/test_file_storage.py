#!/usr/bin/python3
"""
    Test for base FileStorage
"""
import unittest
from models.engine import file_storage
from models import storage
import os
from datetime import datetime
from models.base_model import BaseModel

FileStorage = file_storage.FileStorage


class test_storage(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(file_storage.FileStorage.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(FileStorage.__doc__) > 1)

    def test_of_PEP8_base_model(self):
        self.assertEqual(os.system("pep8 ./models/engine/file_storage.py"), 0)

    def test_of_PEP8_test_base_model(self):
        self.assertEqual(os.system(
            "pep8 tests/test_models/test_engine/test_file_storage.py"), 0)

    def test_shebang(self):
        with open('models/engine/file_storage.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Class cases
    """
    def test_all(self):
        my_objs = storage.all()
        self.assertTrue(type(my_objs), "<class 'dict'>")

    def test_save(self):
        my_file = "file.json"
        os.remove(my_file)
        MyModel = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists(my_file), True)
        os.remove(my_file)

    def test_reload(self):
        MyModel = BaseModel()
        storage.save()
        _dic = storage.reload
        self.assertTrue(type(_dic), "<class 'dict'>")

    def test_attr_path(self):
        self.assertTrue(type(FileStorage._FileStorage__file_path), ".json")

    def test_attr_objects(self):
        self.assertTrue(type(
            FileStorage._FileStorage__objects), dict)
