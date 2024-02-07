#!/usr/bin/python3
"""
console.py

This module houses class HBNBCommand, a subclass of the standard library's Cmd
class. The module launches an interactive command interpreter when executed,
that can handle various commands, that are handled by methods defined in the
HBNBCommand class. The class is primarily intended to manipulate objects in a
file storage.
"""

from airbnb_resc.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines a command interpreter and defines methods that guide
    actions in response to user interactions
    """

    prompt = '(hbtn) '

    def do_create(self, class_name=None):
        """
        Creates a new instance of class BaseModel, saves it (to a JSON file)
        and prints the id.
        """
        if not class_name:
            print("** class name missing **")
        elif class_name in globals() and type(globals()[class_name]) is type:
            instance = globals()[class_name]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """Handles the end-of-file marker"""
        return True

    def do_quit(self, q):
        """Exits the command interpreter"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
