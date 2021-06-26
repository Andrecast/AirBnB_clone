#!/usr/bin/python3
"""
    Test for base model
"""
import unittest
from models import base_model
import os
from datetime import datetime

BaseModel = base_model.BaseModel


class test_base(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        self.assertTrue(len(base_model.BaseModel.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_to_the_class_docstring(self):
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_of_PEP8_base_model(self):
        self.assertEqual(os.system("pep8 ./models/base_model.py"), 0)

    def test_of_PEP8_test_base_model(self):
        self.assertEqual(os.system(
            "pep8 tests/test_models/test_base_model.py"), 0)

    def test_shebang(self):
        with open('models/base_model.py', 'r') as text:
            line_1 = text.readline()
            self.assertEqual(line_1.strip(), '#!/usr/bin/python3')

    """Class cases
    """
    def test_time(self):
        """
        Test if created_at, updated_at are valid
        """
        then = datetime.now()
        my_model = BaseModel()
        now = datetime.now()
        self.assertTrue(then <= my_model.created_at <= now)
        self.assertTrue(then <= my_model.updated_at <= now)
        self.assertTrue(my_model.created_at <= my_model.updated_at)

    def test_uuid(self):
        """Test if objects have different uuid
        """
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_save(self):
        my_model3 = BaseModel()
        var = my_model3.updated_at
        my_model3.save()
        var2 = my_model3.updated_at
        self.assertNotEqual(var, var2)

    def test_str_method(self):
        """
        Tests __str__ of BaseModel class
        """
        my_model = BaseModel()
        s = "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), s)
