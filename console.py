#!/usr/bin/python3
''' Module for console '''

import cmd
import models
import os
import json
import uuid

#from models.User import User
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    ''' simple command processor for
        Holberton AirBnB recreation
    '''

    prompt = '(hbnb) '
    intro = "AirBnB clone command processor for Holberton School"
    clst = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    # clst is short for class list

    def do_create(self, line):
        "Creates new instance of BaseModel. Saves to JSON when specified"
        if line is None or line == "":
            print("** class name missing **")
            return False
        linearg = line.split()
        try:
            usrinput = eval(linearg[0])()
            usrinput.save()
            print(usrinput.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        "Prints the string instance based on class name and id"
        linearg = line.split()
        if len(linearg) > 1:
            showem = "{}.{}".format(linearg[0], linearg[1])
        if len(linearg) == 0:
            print("** class name missing **")
            return
        if linearg[0] not in self.clst:
            print("** class doesn't exist **")
            return
        if len(linearg) < 2:
            print("** instance id missing **")
            return
#        all_objects = storage.all()
        else:
            for value in storage.all().values():
                ''' find cls, if match, retr as str, appendto list_all '''
                print(value)

    def do_destroy(self, line):
        ''' Deletes instance based on class name and id '''
        "Deletes an instance based on class name and id"
        linearg = line.split()
        if len(linearg) > 1:
            destroyem = "{}.{}".format(linearg[0], linearg[1])
        if len(linearg) == 0:
            print("** class name missing **")
            return
        if linearg[0] not in self.clst:
            print("** class doesn't exist **")
            return
        if len(linearg) < 2:
            print("** instance id missing **")
            return
        else:
            for value in storage.all().values():
                del (value)
#        ''' set retrieved dict and set to all_objects '''
#        all_objects = storage.all()
#        ''' convert class name and id to strings '''
#        if destroyem not in all_objects.keys():
#            print("** no instance found **")
#            return
#        del (all_objects[destroyem])

    def do_all(self, line):
        ''' Print all string instances '''
        "Prints all string instances based or not, on class name"
        linearg = line.split()
        list_all = []
        if len(linearg) == 0:
            for value in storage.all().values():
                ''' retrieve elements from dict as string append to list_all'''
                list_all.append(str(value))
        else:
            ''' check for class name in our clst '''
            if linearg[0] not in self.clst:
                print("** class doesn't exist **")
            else:
                ''' search elements in dict '''
                for value in storage.all().values():
                    ''' find cls, if match, retr as str, appendto list_all '''
                    list_all.append(str(value))
        if list_all != []:
            print(list_all)

    def do_update(self, line):
        "Updates instance from class name and id by adding/updating attribute"
        linearg = line.split()
        if len(linearg) > 1:
            updateem = "{}.{}".format(linearg[0], linearg[1])
        if line is None or line == "" or linearg[0] is None or linearg[0] == "":
            print("** class doesn't exist **")
            return
        if len(linearg) == 0:
            print("** class name missing **")
            return
        if len(linearg) == 1:
            print("** instance id missing **")
            return
#        else:
#            all_objects = storage.all()
#            updateem = "{}.{}".format(linearg[0], linearg[1])
#            ''' if class name or id is not in the retrieved dict keys '''
#            if updateem not in all_objects.keys():
#                print("** no instance found **")
#                return
        if len(linearg) == 2:
            print("** attribute name missing **")
            return
        if len(linearg) == 3:
            print("** value missing **")
            return
        else:
#  PROBLEMS SETTING AND SAVING ATTRIBUTE
#            getem = getattr(self, linearg[2])
#            all_objects = storage.all()
            setattr(updateem, linearg[2], linearg[3])
            storage.all()[updateem].save()

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
