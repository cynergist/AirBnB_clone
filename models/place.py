#!/usr/bin/python3
''' Module for Place '''
from models.base_model import BaseModel


class Place(BaseModel):
    ''' A child class for places '''
    city_id = ""
    ''' city_id is an attribute of Place '''
    user_id = ""
    ''' user_id is an attribute of Place '''
    name = ""
    ''' name is an attribute of Place '''
    number_rooms = 0
    ''' number_rooms is an attribute of Place '''
    number_bathrooms = 0
    ''' number_bathrooms is an attribute of Place '''
    max_guest = 0
    ''' max_guest is an attribute of Place '''
    price_by_night = 0
    ''' price_by_night is an attribute of Place '''
    latitude = 0.0
    ''' latitude is an attribute of Place '''
    longitude = 0.0
    ''' longitude is an attribute of Place '''
    amenity_ids = []
    ''' amenity_ids is an attribute of Place '''
