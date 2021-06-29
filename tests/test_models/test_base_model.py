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
        before = datetime.now()
        my_model3 = BaseModel()
        my_model3.save()
        self.assertNotEqual(before, my_model3.updated_at)

    def test_str_method(self):
        """
        Tests __str__ of BaseModel class
        """
        my_model = BaseModel()
        s = "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), s)

    def test_normal(self):
        my_model4 = BaseModel()
        my_model4.name = "Holberton"
        my_model4_dict = my_model4.to_dict()
        self.assertEqual('name' in my_model4_dict, True)

    def test_if_attr_exist(self):
        my_model5 = BaseModel()
        self.assertTrue(hasattr(my_model5, "id"))
        self.assertTrue(hasattr(my_model5, "created_at"))
        self.assertTrue(hasattr(my_model5, "updated_at"))

    def test_when_the_dict_is_empty(self):
        my_dict = {}
        my_model6 = BaseModel(**my_dict)
        my_model6_dict = my_model6.to_dict()
        self.assertEqual('id' in my_model6_dict, True)
        self.assertEqual('created_at' in my_model6_dict, True)
        self.assertEqual('updated_at' in my_model6_dict, True)

    def test_when_the_dict_is_no_empty(self):
        my_model7 = BaseModel()
        my_model7.name = "Holberton"
        my_model7.save()
        my_model7_json = my_model7.to_dict()
        my_new_model = BaseModel(**my_model7_json)
        self.assertTrue(
            type(my_model7.created_at), "<class 'datetime.datetime'>")
        self.assertTrue(
            type(my_model7.updated_at), "<class 'datetime.datetime'>")

    def test_id(self):
        object1 = BaseModel()
        object2 = BaseModel()
        object1.name = "prueba"
        self.assertEqual(object1.name, "prueba")
        self.assertNotEqual(object1.id, object2.id)

    def test_created(self):
        object1 = BaseModel()
        object2 = BaseModel()
        self.assertNotEqual(object1.created_at, object2.created_at)
        self.assertNotEqual(object1.updated_at, object2.updated_at)
        self.assertNotEqual(object1.created_at, object1.updated_at)
        self.assertNotEqual(object2.created_at, object2.updated_at)

    def test_to_dict(self):
        object1 = BaseModel()
        object2 = object1.to_dict()
        self.assertEqual(object2["updated_at"], object1.to_dict["updated_at"])