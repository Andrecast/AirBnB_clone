#!/usr/bin/python3

"""The command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The class entry point of the command interpreter
    """
    prompt = "(hbnb) "
    list_of_class = [
        'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

    def do_quit(self, args):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program

        """
        return True

    def emptyline(self):
        """Empty line shouldn’t execute anything

        """
        pass

    def do_create(self, args):
        """Create Creates a new instance of BaseModel
        """

        if args in HBNBCommand.list_of_class:
            _instance = eval(args)()
            print(_instance.id)
        elif args == '':
            print("** class name missing **")
        elif args not in HBNBCommand.list_of_class:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance

        """
        if args:
            list_class_id = args.split()
            if list_class_id[0] in HBNBCommand.list_of_class:
                if len(list_class_id) == 2:
                    all_objs = storage.all()
                    _id = "{}.{}".format(list_class_id[0], list_class_id[1])
                    if any(_id == keys for keys in all_objs.keys()):
                        print(all_objs[_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print(""" ** class name missing ** """)

    def do_destroy(self, args):
        """Deletes an instance

        """
        if args:
            list_class_id = args.split()
            if list_class_id[0] in HBNBCommand.list_of_class:
                if len(list_class_id) == 2:
                    all_objs = storage.all()
                    _id = "{}.{}".format(list_class_id[0], list_class_id[1])
                    if _id in all_objs:
                        all_objs.pop(_id)
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """Prints all string representation of all instances

        """
        if args or args == '' or args in HBNBCommand.list_of_class:
            all_objs = storage.all()
            my_list = []
            for value in all_objs.values():
                my_list.append(str(value))
            print(my_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance

        """
        if args:
            my_list = args.split()
            if my_list[0] in HBNBCommand.list_of_class:
                if len(my_list) > 1:
                    if len(my_list) > 2:
                        all_objs = storage.all()
                        _id = "{}.{}".format(
                            my_list[0], my_list[1])
                        if _id in all_objs:
                            setattr(all_objs[_id], my_list[2], my_list[3])
                            storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** value missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    """The code should not be executed when imported

    """
    HBNBCommand().cmdloop()
