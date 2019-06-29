#!/usr/bin/python3
''' Module for BaseModel '''

import json
import uuid
from datetime import datetime


class BaseModel():
    ''' Parent class/file for future classes in separate files '''
    def __init__(self, *args, **kwargs):
        '''
        Creates instance of BaseModel
        Arg1: None
        Arg2: Current key/values in dictionary
        '''
        self.id = str(uuid.uuid4())
        ''' id is an attribute of the class
            uuid4 function generates random unique user id
        '''
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        ''' created_at is datetime, assigns when instance created
            updated_at is datetime as above and updates on object change
        '''

        for key, value in kwargs.items():
            if value is not None:
                continue
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()

    def __str__(self):
        ''' String representation of class name, id, and __dict__ '''
        return ('[{}] ({}) {}'
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        ''' Instance that updates updated_at with current datetime '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Returns dictionary representation of keys/values '''
        self.__dict__['_class_'] = 'self.__dict__'
        return self.__dict__
