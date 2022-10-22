import sys

from offsync import cli

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)

    if argc != 1 and args[1] == "add":
        cli.add_profile()
    elif argc != 1 and args[1] == "remove":
        cli.remove_profile()
    else:
        cli.get_password()
