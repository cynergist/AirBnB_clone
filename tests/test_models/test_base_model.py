#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
import models

from models.base_model import BaseModel
''' Unittest for base_model '''


class SimplisticTest(unittest.TestCase):
    ''' Unittest for ensure testing environment works '''
    def test(self):
        self.assertTrue(True)


class TestBaseModel(unittest.TestCase):
    ''' Unittest for base_model '''

    a = BaseModel()
    b = BaseModel()

    def test_class(self):
        self.assertTrue(True)

    def test_class_type(self):
        ''' Unittest for correct class type '''
        self.assertTrue(type(self.a), BaseModel)

    def test_instantiation(self):
        ''' Unittest for instantiation of class '''
        self.assertTrue(self.b)

    def test_id_isinstance(self):
        ''' Unitest for id as public instance '''
        self.assertIsInstance(self.a.id, type(self.a.id))

    def test_uniq_id(self):
        ''' Unittest for unique id '''
        random = [BaseModel().id for x in range(999)]
        len(set(random)) == len(random)
        self.assertTrue(self, BaseModel().id)

    def test_datetime(self):
        ''' Unittest for creation of datetime '''
        self.a.save()
        self.assertNotEqual(self.a.created_at, self.a.updated_at)

    def test_id_creation(self):
        ''' Unitest for creation of id '''
        self.assertTrue(self.a.id)
        self.assertTrue(self.b.id)
        self.assertNotEqual(self.b.id, self.a.id)

    def test_to_dict(self):
        ''' Unittest for return of dictionary representation of key/values '''
        self.assertTrue(type(self.a.to_dict() is dict))
        self.assertTrue(type(self.b.to_dict() is dict))

    def test_dict_serial(self):
        ''' Unittest for serialization of dictionary to json format '''

        '''hasattr() will check for class even if instance is not from class'''

if __name__ == '__main__':
    unittest.main()
