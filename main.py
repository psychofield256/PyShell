#!/usr/bin/env python
"""
Try to make a small shell, with customizable commands.

Made on May 8th 2016 by Yacine Cheikhrouhou.
"""

# import pygame

from collections import deque

from commands import command_list


# integrate important functions
exec(open("sys_commands.py").read())

commands = {
    # those 2 are in sys_commands.py
    "exit": exit,
    "help": help,
}

commands.update(command_list)


running = True


def main():
    print("Type 'help' to see the list of commands.")
    while running:
        line = input(">>")
        # extract the command and the args
        # command = line.split()[0]
        # args = line.replace(command + " ", "")
        line = deque(line.split())
        if line:
            command = line.popleft()
            args = " ".join(line)
            if command in commands:
                try:
                    if args:
                        value = commands[command](args)
                        if value is not None: print(value)
                    else:
                        value = commands[command]()
                        if value is not None: print(value)
                except Exception as e:
                    print("An error occured:", e)
            else:
                print("Unknown command.")
                print(commands["help"]())


if __name__ == "__main__":
    main()
    # for fun in c.locals():
    #    print(fun)
