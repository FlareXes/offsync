import sys

from pyperclip import copy

from offsync import cli
from offsync.storage import Database
from offsync.ui import set_mode

Database().init_database()

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    continuous = argc == 3 and args[2] == "c"

    if argc > 1 and args[1] not in ["add", "remove", "update", "prompt", "pwned", "help"] or argc == 3 and args[
        2] != "c":
        cli.usage()
        print(">>> Invalid Option! <<<")
        sys.exit(2)

    if argc > 3:
        cli.usage()
        print(">>> Too Many Arguments! <<<")
        sys.exit(2)

    if argc != 1 and args[1] == "add":
        set_mode("Save Mode")
        if continuous:
            cli.add_profiles()
        else:
            cli.add_profile()

    elif argc != 1 and args[1] == "remove":
        set_mode("Delete Mode")
        if continuous:
            cli.remove_profiles()
        else:
            cli.remove_profile()

    elif argc != 1 and args[1] == "update":
        set_mode("Update Mode")
        if continuous:
            cli.usage()
            print(">>> Unsupported Argument `c` <<<")
            sys.exit(2)
        else:
            cli.change_password()

    elif argc != 1 and args[1] == "pwned":
        if continuous:
            cli.usage()
            print(">>> Unsupported Argument `c` <<<")
            sys.exit(2)
        else:
            cli.pwned_profiles()

    elif argc != 1 and args[1] == "help":
        cli.usage()

    else:
        set_mode("View Mode")
        if argc == 2 and args[1] == "prompt":
            cli.get_password(prompt=True)
        else:
            cli.get_password()

    copy("")
