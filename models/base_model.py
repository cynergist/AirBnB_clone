#!/usr/bin/python3
''' Module for BaseModel '''

import json
import uuid
from datetime import datetime


class BaseModel():
    ''' Parent class/file for future classes in separate files '''
    def __init__(self):
        '''
        Creates instance of BaseModel
        Arg1: variable id is initialized at None
        '''
        self.id =  uuid.uuid4()
        ''' id is an attribute of the class
            created_at is datetime, assigns when instance created
            updated_at is datetime as above and updates on object change
        '''
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.now()
        ''' uuid4 function generates random unique user id '''
        self.__dict__ = self.dict
        self.__class__ = self.dict

    def __str__(self):
        ''' String representation of class name, id, and __dict__ '''
        return ('[{}] ({}) {}'.format(self, self.id, self.dict))

    def save(self):
        ''' Instance that updates updated_at with current datetime '''
        self.updated_at = datetime.now(tz=None)

    def to_dict(self):
        ''' Returns dictionary representation of keys/values '''
        '''
        return {'my_number': , 'name': , 'updated_at': self.updated_at,
                'id': self.id, 'created_at': self.created_at}
        '''
