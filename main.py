import sys

from offsync import cli

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)

    if argc != 1 and args[1] == "add":
        if argc > 2 and args[2] == "c":
            cli.add_profiles()
        else:
            cli.add_profile()
    elif argc != 1 and args[1] == "remove":
        if argc > 2 and args[2] == "c":
            cli.remove_profiles()
        else:
            cli.remove_profile()
    else:
        cli.get_password()
