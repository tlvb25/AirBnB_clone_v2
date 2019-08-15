#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Interpreter for AirBnB clone"""

    prompt = '(hbnb) '
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review}

    def do_quit(self, line):
        """Exits the program
        Args:
            line - the user inputted string
        """

        return True

    def emptyline(self):
        """Skips the line if nothing is entered"""

        pass

    def do_EOF(self, line):
        """Exits the program
        Args:
            line - the user inputted string
        """

        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Args:
            line - user input
        """

        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            obj = eval("{}()".format(my_list[0]))
            for i in my_list[1:]:
                new_list = i.split("=")
                key = new_list[0]
                value = new_list[1]
                value = value.replace('_',' ')
                if hasattr(obj, key):
                    setattr(obj, key, eval(value))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id
        Args:
            line - user input
        """

        if not line or line is "":
            print('** class name missing **')
            return
        args = line.split()
        if len(args) == 2:
            if args[0] in self.classes:
                key = args[0] + '.' + args[1]
                rec_of_instances = storage.all()
                if key not in rec_of_instances:
                    print("** no instance found **")
                    return
                else:
                    print(rec_of_instances[key])
                    return
            else:
                print("** class doesn't exist **")
                return
        elif len(args) == 1:
                print("** instance id missing **")
                return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Args:
            line - user input
        """

        rec_of_instances = storage.all()
        if not line or line == "":
            print('** class name missing **')

        args = line.split()
        if len(args) == 2:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')
                return
            else:
                del rec_of_instances[key]
                storage.save()

        elif len(args) == 1:
            print('** instance id missing **')
            return

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Args:
            line - user input
        """

        rec_of_instances = storage.all()
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')
            else:
                a3 = args[3].strip('\"')
                if hasattr(key, args[2]) is True:
                    attr_type = type(getattr(key, args[2]))
                    if attr_type == int:
                        setattr(rec_of_instances[key], args[2], int(a3))
                        storage.save()
                    elif attr_type == float:
                        setattr(rec_of_instances[key], args[2], float(a3))
                        storage.save()
                else:
                    setattr(rec_of_instances[key], args[2], a3)
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        Args:
            line - user input
        """
        key_list = []
        instances = storage.all()
        if len(line) == 0:
            for v in instances.values():
                key_list.append(v.__str__())
            print(key_list)
            return
        line_list = line.split()
        if line_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        for v in instances.values():
            if line_list[0] == v.__class__.__name__:
                key_list.append(v.__str__())
        print(key_list)

    def default(self, line):
        print('default({})'.format(line))
        return cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
