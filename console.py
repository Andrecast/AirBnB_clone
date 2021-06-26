#!/usr/bin/python3

"""The command interpreter.

"""
import cmd

class HBNBCommand(cmd.Cmd):
    """The class entry point of the command interpreter.

    """
    prompt = "(hbnb) "
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

if __name__ == '__main__':
    """The code should not be executed when imported

    """
    HBNBCommand().cmdloop()
