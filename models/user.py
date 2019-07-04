#!/usr/bin/python3
''' Module for User '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' A child class/file for a user '''

    email = ""
    ''' email is an attribute of the class '''
    password = ""
    ''' password is an attribute of the class '''
    first_name = ""
    ''' first_name is an attribute of the class '''
    last_name = ""
    ''' last_name is an attribute of the class '''
