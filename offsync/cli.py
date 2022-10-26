from offsync.clipboard import copy
from offsync.password import generate_password
from offsync.profile import create_profile
from offsync.security import get_master_password
from offsync.storage import load_profiles, delete_profile
from offsync.ui import _Table


def _list_profiles():
    table = _Table()
    for _id, profile in load_profiles().items(): table.add_row(_id, profile)
    table.tabulate()


def _select_profile(_id=False):
    ask = input("\nq to exit > ")
    if ask == "v" or ask == "view":
        _list_profiles()
    elif ask == "q" or ask == "quit" or ask == "exit":
        exit(0)
    elif _id:
        return ask
    else:
        try:
            return load_profiles()[ask]
        except KeyError as e:
            print("Invalid Input!")


def add_profile():
    site, username, counter, length = input("Site: "), input("Username / E-Mail: "), input("Counter (1): "), input(
        "Length (16): ")
    if length.strip(" ") == "": length = 16
    if counter.strip(" ") == "": counter = 1
    create_profile(site, username, counter, length)


def add_profiles():
    while True:
        add_profile()
        print("")
        ask = input("Continue (Y/n): ").lower()
        print("")

        if not ask == "" or ask == "y":
            _list_profiles()
            break


def remove_profile():
    _list_profiles()
    _id = _select_profile(_id=True)
    delete_profile(_id)
    _list_profiles()


def remove_profiles():
    _list_profiles()
    print("\nEnter S.No. Of All Profiles You Want To Remove Seperated By Coma ','")
    print("For Example: > 1, 2, 3, 4")
    print("NOTE: Any Non-Numeric Value Will Terminate The Process")

    ids = []

    try:
        ids = [i if i.isdigit() else int(i) for i in input("> ").replace(" ", "").split(",")]
    except ValueError as e:
        print("\nInvalid Input: ", e)
        exit(1)

    for _id in ids:
        delete_profile(_id)
    _list_profiles()


def get_password():
    mp_hash = get_master_password()
    _list_profiles()
    while True:
        profile = _select_profile()
        if profile is None: continue
        passwd = generate_password(profile, mp_hash)
        copy(passwd)
        print("Copied To Clipboard")
