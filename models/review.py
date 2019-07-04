#!/usr/bin/python3
''' Module for Review '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' A child class for reviews '''
    place_id = ""
    ''' place_id is an attribute of Review '''
    user_id = ""
    ''' user_id is an attribute of Review '''
    text = ""
    ''' text is an attribute of Review '''
