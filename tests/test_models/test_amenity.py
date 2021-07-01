#!/usr/bin/python3
"""
    Test for user
"""
import unittest
from models import amenity
import os
Amenity = amenity.Amenity


class test_user(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(amenity.Amenity.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(Amenity.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_of_PEP8_base_model(self):
        self.assertEqual(os.system("pep8 ./models/amenity.py"), 0)

    def test_of_PEP8_test_base_model(self):
        self.assertEqual(os.system(
            "pep8 tests/test_models/test_amenity.py"), 0)

    def test_shebang(self):
        with open('models/amenity.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Class cases
    """
    def test_instances(self):
        MyModel = Amenity()
        MyModel.name = "Laurant"
        self.assertIsInstance(MyModel, Amenity)
        self.assertTrue(MyModel.name, "<class 'Amenity'>")
        self.assertEqual(type(MyModel.name), str)
