#!/usr/bin/python3
"""
    Test for user
"""
import unittest
from models import review
import os
Review = review.Review


class test_user(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(review.Review.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(Review.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(Review.to_dict.__doc__) > 1)

    def test_of_PEP8_base_model(self):
        self.assertEqual(os.system("pep8 ./models/review.py"), 0)

    def test_of_PEP8_test_base_model(self):
        self.assertEqual(os.system(
            "pep8 tests/test_models/test_review.py"), 0)

    def test_shebang(self):
        with open('models/review.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Class cases
    """
    def test_instances(self):
        MyModel = Review()
        MyModel.name = "Laurant"
        self.assertIsInstance(MyModel, Review)
        self.assertTrue(MyModel.name, "<class 'Review'>")
        self.assertEqual(type(MyModel.name), str)
