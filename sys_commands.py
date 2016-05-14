"""
The commands who need an access to a part of the shell.

They can access global variables.
That's all for now, but you can find other uses.
There won't be error if they access to main code, because the
code here will be executed from main directly.

So code checking tools like pylint will detect fake errors.
"""

# these 2 commands can't be imported because they need an
# access to the "system"
# exit needs a global variable, and help needs the command list
def exit():
    """Quit the shell."""
    global running
    running = False


def help(commands_str=None):
    """The help for every command"""
    # if one or more command is passed in arguments give their doc
    if commands_str:
        ret_value = ""
        for command in commands_str.split():
            if command in commands:
                ret_value += "%s: %s\n" % (command, commands[command].__doc__)
            else:
                ret_value += "Unknown command.\n"
    else:
        ret_value = "command list:\n"
        for c in commands:
            ret_value += "%s: %s\n" % (c, commands[c].__doc__)

    return ret_value
