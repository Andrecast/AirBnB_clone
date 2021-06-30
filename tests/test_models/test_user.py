#!/usr/bin/python3
"""
    Test for user
"""
import unittest
from models import user
import os
User = user.User

class test_user(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(user.User.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(User.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_of_PEP8_base_model(self):
        self.assertEqual(os.system("pep8 ./models/user.py"), 0)

    def test_of_PEP8_test_base_model(self):
        self.assertEqual(os.system(
            "pep8 tests/test_models/test_user.py"), 0)

    def test_shebang(self):
        with open('models/user.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')
        
    """Class cases
    """
    def test_instances(self):
        MyModel = User()
        MyModel.name = "Laurant"
        self.assertIsInstance(MyModel.name, User)
