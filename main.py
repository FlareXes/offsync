import sys

from offsync import cli

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 1 and args[1] == "add":
        cli.add_profile()
    else:
        cli.get_password()
