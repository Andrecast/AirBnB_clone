#!/usr/bin/python3
"""
    Test for user
"""
import unittest
from models import city
import os
City = city.City


class test_city(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(city.City.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(City.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_of_PEP8_base_model(self):
        self.assertEqual(os.system("pep8 ./models/city.py"), 0)

    def test_of_PEP8_test_base_model(self):
        self.assertEqual(os.system(
            "pep8 tests/test_models/test_city.py"), 0)

    def test_shebang(self):
        with open('models/city.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Class cases
    """
    def test_instances(self):
        MyModel = City()
        MyModel.name = "Laurant"
        self.assertIsInstance(MyModel, City)
        self.assertTrue(MyModel.name, "<class 'City'>")
        self.assertEqual(type(MyModel.name), str)
