#!/usr/bin/python3
"""
    Test for user
"""
import unittest
from models import state
import os
State = state.State


class test_user(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(state.State.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(State.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(State.to_dict.__doc__) > 1)

    def test_of_PEP8_base_model(self):
        self.assertEqual(os.system("pep8 ./models/state.py"), 0)

    def test_of_PEP8_test_base_model(self):
        self.assertEqual(os.system(
            "pep8 tests/test_models/test_state.py"), 0)

    def test_shebang(self):
        with open('models/state.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Class cases
    """
    def test_instances(self):
        MyModel = State()
        MyModel.name = "Laurant"
        self.assertIsInstance(MyModel, State)
        self.assertTrue(MyModel.name, "<class 'State'>")
        self.assertEqual(type(MyModel.name), str)
