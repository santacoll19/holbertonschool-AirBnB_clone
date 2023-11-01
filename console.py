#!/usr/bin/python3
"""Console module"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import models

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

    def do_create(self, args):
        """Create a new instance of a class and save it to the JSON file"""
        if args == "":
            print("** class name missing **")
        else:
            args_list = args.split()
            class_name = args_list[0]
            if class_name not in models.CLASS_DICT:
                print("** class doesn't exist **")
            else:
                new_instance = models.CLASS_DICT[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        """Show the string representation of an instance"""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in models.CLASS_DICT:
                print("** class doesn't exist **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = args_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in models.CLASS_DICT:
                print("** class doesn't exist **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = args_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    del models.storage.all()[key]
                    models.storage.save()

    def do_all(self, args):
        """Print all string representations of all instances or of a specific class"""
        args_list = args.split()
        obj_list = []
        if len(args_list) == 0:
            for key in models.storage.all():
                obj_list.append(str(models.storage.all()[key]))
            print(obj_list)
        else:
            class_name = args_list[0]
            if class_name not in models.CLASS_DICT:
                print("** class doesn't exist **")
            else:
                for key in models.storage.all():
                    if key.split(".")[0] == class_name:
                        obj_list.append(str(models.storage.all()[key]))
                print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args_list = arg.split()
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
