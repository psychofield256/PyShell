"""
List of the commands used in the shell.

TODO:
-rm
"""

import os

from functools import reduce


def say(msg=""):
    """Prints the message to the screen."""
    print(msg)


def add(str_args):
    """Simple addition."""
    args = str_args.split()
    print(sum([int(arg) for arg in args]))


def sub(str_args):
    """Simple subtraction. Error if more or less than 2 args."""
    # this part raises an error if there are not 2 args
    # it's on purpose, the shell will handle the error
    x, y = str_args.split()
    print(int(x) - int(y))


def mul(str_args):
    "Simple multiplication."
    args = str_args.split()
    print(reduce(lambda x, y: x * y, args))


def mkdir(name):
    """Create a directory."""
    os.mkdir(name)


def mkfile(name):
    """Create a file."""
    open(name, "a").close()


def pwd():
    """Print working directory."""
    print(os.getcwd())


def cd(path):
    """Change directory."""
    os.chdir(path)


def rm(file):
    """Delete a file or an empty directory."""
    if os.path.isfile(file):
        os.remove(file)
    elif os.path.isdir(file):
        try:
            os.rmdir(file)
        except OSError:
            print("the folder is not empty and can't be deleted")
    else:
        print("no such file or directory")


command_list = {
    "say": say,
    "add": add,
    "sub": sub,
    "mul": mul,

    "mkdir": mkdir,
    "mkfile": mkfile,
    "pwd": pwd,
    "cd": cd,
    "rm": rm,
}
