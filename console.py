#!/usr/bin/python3
"""Console module"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """HBHBCommand class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit exit command"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit"""
        return True

    def emptyline(self):
        """Empty line + ENTER do not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
