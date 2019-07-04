#!/usr/bin/python3
''' Module for City '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' A child class for a city '''
    state_id = ""
    name = ""
