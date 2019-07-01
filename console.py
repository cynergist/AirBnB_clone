#!/usr/bin/python3
''' Module for console '''

import cmd
import models
import os
import json
import uuid
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' simple command processor for
        Holberton AirBnB recreation
    '''

    prompt = '(hbnb)'
    intro = "AirBnB clone command processor for Holberton School"

    def do_create(self, line):
        "Creates new instance of BaseModel. Saves to JSON when specified"
        create = BaseModel()
        create.name = line
        create.save()
#        return

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
