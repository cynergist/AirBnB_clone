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

    prompt = '(hbnb)'
    intro = "AirBnB clone command processor for Holberton School"

    def do_create(self, line):
        "Creates new instance of BaseModel. Saves to JSON when specified"
        if line is None or line == "":
            print("** class name missing **")
            return False
        classes = line.split()
        try:
            usrinput = eval(classes[0])()
            usrinput.save()
            print(usrinput.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        "Prints the string instance based on class name and id"
        linearg = shlex.split(line)
        if line is None or line == "":
            print("** class name missing **")
            return False
        all_objects = storage.all()
        checkem = "{}.{}".format(linearg[0], linearg[1])
        ''' if class name or id is not in the retrieved dict keys '''
        if checkem not in all_objects.keys():
            print("No instance found")
            return
        print(all_objects[checkem])

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
