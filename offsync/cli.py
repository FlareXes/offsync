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
    site, username, counter, length = input("Site: "), input("Username / E-Mail: "), input("Counter: "), input(
        "Length: ")
    if length.strip(" ") == "": length = 16
    create_profile(site, username, counter, length)


def remove_profile():
    _list_profiles()
    _id = _select_profile(_id=True)
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
