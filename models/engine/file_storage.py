#!/usr/bin/python3
''' Module for FileStorage '''

import json
import models.base_model import BaseModel


class FileStorage():
    ''' class serializes instances to JSON file and
    deserializes JSON file to instances
    '''
    def __init__(self):
        '''Creates instance of FileStorage'''
        __file_path = 'file.json'
        __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        with open("file.json", "w") as serialized_file:
            json.dump(obj, serialized_file)

    def reload(self):

        else:
            do nothing
