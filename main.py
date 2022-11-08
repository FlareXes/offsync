import sys

from offsync import cli
from offsync.cli import usage

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    continuous = argc == 3 and args[2] == "c"

    if argc > 1 and args[1] not in ["add", "remove"] or argc == 3 and args[2] != "c":
        usage()
        print(">>> Invalid Option! <<<")
        sys.exit(2)

    if argc > 3:
        usage()
        print(">>> Too Many Arguments! <<<")
        sys.exit(2)

    if argc != 1 and args[1] == "add":
        if continuous:
            cli.add_profiles()
        else:
            cli.add_profile()
    elif argc != 1 and args[1] == "remove":
        if continuous:
            cli.remove_profiles()
        else:
            cli.remove_profile()
    elif argc != 1 and args[1] == "help":
        usage()
    else:
        cli.get_password()
