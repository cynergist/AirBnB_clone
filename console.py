#!/usr/bin/python3
''' Module for console '''

import cmd
import models
import os
import json
import uuid
import shlex

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
        linearg = shlex.split(line)
        try:
            usrinput = eval(linearg[0])()
            usrinput.save()
            print(usrinput.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        "Prints the string instance based on class name and id"
        linearg = shlex.split(line)
        if line is None or line == "":
            print("** class doesn't exist **")
            return
        if len(linearg) == 0:
            print("** class name missing **")
            return
        if linearg[0] not in self.clst:
            print("** class doesn't exist **")
            return
        if len(linearg) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        checkem = "{}.{}".format(linearg[0], linearg[1])
        ''' if class name or id is not in the retrieved dict keys '''
        if checkem not in all_objects.keys():
            print("** no instance found **")
            return
        print(all_objects[checkem])

    def do_destroy(self, line):
        "Deletes an instance based on class name and id"
        linearg = shlex.split(line)
        if line is None or line == "":
            print("** class doesn't exist **")
            return False
        if linearg[0] == "":
            print("** class name missing **")
            return
        if len(linearg) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        deleteem = "{}.{}".format(linearg[0], linearg[1])
        if deleteem not in all_objects.keys():
            print("** no instance found **")
            return
        del (all_objects[deleteem])

    def do_all(self, line):
        "Prints all string instances based or not, on class name"
        linearg = shlex.split(line)
        list_all = []
        if line is None or line == "":
            print("** class doesn't exist **")
            return
        if len(linearg) == 0:
            for value in storage.all():
                list_all.append(str(storage.all()[value]))
                return
        else:
            if linearg[0] not in self.clst:
                print("** class doesn't exist **")
            else:
                for value in storage.all():
                    if value.startswith(linearg[0]):
                        list_all.append(str(storage.all()[value]))
        if list_all != []:
            print(list_all)

    def do_update(self, line):
        "Updates instance from class name and id by adding/updating attribute"
        linearg = shlex.split(line)
        if line is None or line == "":
            print("** class doesn't exist **")
            return
        if len(linearg) == 0:
            print("** class name missing **")
            return
        if len(linearg) == 1:
            print("** instance id missing **")
            return
        else:
            all_objects = storage.all()
            updateem = "{}.{}".format(linearg[0], linearg[1])
            ''' if class name or id is not in the retrieved dict keys '''
            if updateem not in all_objects.keys():
                print("** no instance found **")
                return
        if len(linearg) == 2:
            print("** attribute name missing **")
            return
        if len(linearg) == 3:
            print("** value missing **")
            return
#        else:
#            setattr(, linearg[0], linearg[1])
#            storage.all()[updateem].save()

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
