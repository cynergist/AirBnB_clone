#!/usr/bin/python3
''' Module for console '''

import cmd
import models
import os
import json
import uuid

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
            usrinput = (eval(classes[0]))()
#            create = BaseModel()
#            create.name = classes[1]
            usrinput.save()
            print(usrinput.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        "Prints the string representation of an instance based on class name and id"
        if line is None or line == "":
            print("** class name missing **")
            return False
        classes = line.split()


    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
