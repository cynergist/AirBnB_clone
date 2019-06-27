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
        ''' id here is an attribute of the class '''
        id = uuid.uuid4()
        ''' uuid4 function generates random unique user id '''
        str(id)
        print("{}\n".format(id))
