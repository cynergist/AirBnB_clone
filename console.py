#!/usr/bin/python3
''' Module for console '''

import cmd
import models


class HBNBCommand(cmd.Cmd):
    ''' simple command processor for
        Holberton AirBnB recreation
    '''

    prompt = '(hbnb)'
    intro = "AirBnB clone command processor for Holberton School"

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
