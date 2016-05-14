# PyShell
Small python shell.

Open commands.py to see existing commands and create your own.
Basically, they're just python functions in the command_list dict.
To create your own, you can define new functions and add their keys in command_list.
They don't need to have the same name and key, it's just that I didn't need new names.
You can define functions used by other functions, and keep it private, by not creating a key in command_list.

In sys_commands.py, the functions can access global variables from main.py
That's why exit or help are in sys_commands.py.
You can write your own sys commands, but you need to understand the code of main.py first
in order to use it.