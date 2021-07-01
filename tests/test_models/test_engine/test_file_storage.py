#!/usr/bin/python3
"""
    Test for base FileStorage
"""
from models.engine.file_storage import FileStorage
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
        self.assertTrue(len(file_storage.FileStorage.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(file_storage.FileStorage.__doc__) > 1)

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
        object = storage.all()
        self.assertIsInstance(object, dict)

    def test_new(self):
        pass

    def test_save(self):
        file = "file.json"
        self.assertFalse(os.path.exists(file))
        FileStorage._FileStorage__file_path = "file.json"
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists(file))
        os.remove(file)

    def test_reload(self):
        pass
