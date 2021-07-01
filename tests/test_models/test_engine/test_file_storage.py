#!/usr/bin/python3
""" Import unittest and created a class for unit test """
import os
from datetime import datetime
import unittest
from models.base_model import BaseModel
import models.base_model
from models.engine.file_storage import FileStorage
import models


class TestStorageDocumentation(unittest.TestCase):
    """ Create a tests for the file storage in documentation
    and requirements """

    def test_style_pep8_model(self):
        """ PEP8 python style """
        style_model = os.system("pep8 models/engine/file_storage.py")
        self.assertEqual(style_model, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        style_test = os.system("pep8 tests/test_models/test_engine\
/test_file_storage.py")
        self.assertEqual(style_test, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/engine/file_storage.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_engine/test_file_storage.py\
", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.engine.file_storage.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(FileStorage.__doc__) != 0)

    def test_methods_doc(self):
        """ Methods with sufficient documentation """
        self.assertTrue(len(FileStorage.all.__doc__) != 0)
        self.assertTrue(len(FileStorage.new.__doc__) != 0)
        self.assertTrue(len(FileStorage.save.__doc__) != 0)
        self.assertTrue(len(FileStorage.reload.__doc__) != 0)


class TestStorage(unittest.TestCase):
    """ Create a tests for the file storage in edge cases """
    def test_attribute_path(self):
        """ Check to the path to the JSON file that is a private
            class attributes """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertTrue(FileStorage._FileStorage__file_path != 0)
        self.assertTrue(type(FileStorage._FileStorage__file_path) is str)

    def test_attribute_class_objects(self):
        """Check to the dictionary will store all objects that is a private"""
        self.assertTrue(type(FileStorage._FileStorage__objects) is dict)

    def test_all(self):
        """ Check that method returns the dictionary __objects """
        object = models.storage.all()
        self.assertIsInstance(object, dict)

    def test_new(self):
        """ Check that method sets in __objects the obj with key
            <obj class name>.id """
        pass

    def test_save_exists(self):
        """ Serialize __objects to the JSON file """
        file = "obj.json"
        self.assertFalse(os.path.exists(file))
        FileStorage._FileStorage__file_path = "obj.json"
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists(file))
        os.remove(file)

    def test_reload(self):
        """ Deserialize the JSON file to __objects """
        pass
