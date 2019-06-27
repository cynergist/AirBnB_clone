#!/usr/bin/python3
''' Module for BaseModel '''

import json
import uuid


class BaseModel():
    ''' Parent class/file for future classes in separate files '''
    def __init__(self, id=None):
        '''
        Creates instance of BaseModel
        Arg1: variable id is initialized at None
        '''
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        ''' id is an attribute of the class
            created_at is datetime, assigns when instance created
            updated_at is datetime as above and updates on object change
            '''
        id = uuid.uuid4()
        ''' uuid4 function generates random unique user id '''
        print ("string representation of uuid4() are : ")
        print (repr(id.str))
        print ("byte representation : ")
        print (repr(id.bytes))
        """
        str(id)
        """
