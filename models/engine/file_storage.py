#!/usr/bin/python3
''' Module for FileStorage '''

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    ''' class serializes instances to JSON file and
    deserializes JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}
    clst = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    # clst is short for class list

    def all(self):
        ''' Public instance that returns dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' Public instance that sets in __objects the obj with key '''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]\
            = obj

    def save(self):
        ''' Public instance that serializes __objects to __file_path '''
        dict_a = {}
        for key, value in self.__objects.items():
            dict_a[key] = value.to_dict()
        with open('file.json', 'w') as serialized_file:
            serialized_file.write(json.dumps(dict_a))

    def reload(self):
        ''' Public instance that deserializes __file_path to __objects '''
        if path.isfile('file.json'):
            with open('file.json', 'r') as deserialized_file:
                dfile = json.load(deserialized_file)
                for key, value in dfile.items():
                    if value['__class__'] in self.clst:
                        new_obj = eval(value['__class__'])(**value)
                        self.__objects[key] = new_obj
