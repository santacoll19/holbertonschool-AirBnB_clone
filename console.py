#!/usr/bin/python3
"""Console module"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User

storage = FileStorage()
storage.reload()


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if len(arg) == 0:
            for value in storage.all().values():
                print(value)
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if key.split(".")[0] == "BaseModel":
                    print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if args_list[0] not in FileStorage.CLASS_DICT:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            return
        if len(args_list) == 3:
            print("** value missing **")
            return
        setattr(storage.all()[key], args_list[2], args_list[3].strip("\""))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
