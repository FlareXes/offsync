from typing import Dict

from offsync.clipboard import copy
from offsync.password import generate_password
from offsync.profile import create_profile
from offsync.security import get_master_password
from offsync.storage import load_profiles, delete_profile
from offsync.ui import _Table, get_mode


def _list_profiles(info: bool = True) -> None:
    table = _Table()
    profiles = load_profiles().items()

    for _id, profile in profiles: table.add_row(_id, profile)

    if len(profiles) == 0:
        table.tabulate(info=False)
        exit(0)

    table.tabulate(info)


def _select_profile(only_id: bool = False) -> Dict[str, str] | str | None:
    ask = input(f"\n{get_mode()} > ")
    if ask == "v" or ask == "view":
        _list_profiles()
        return None
    elif ask == "q" or ask == "quit" or ask == "exit":
        exit(0)
    elif only_id:
        return ask
    else:
        try:
            return load_profiles()[ask]
        except KeyError as e:
            print("Invalid Input!")
            return None


def add_profile() -> None:
    site, username, counter, length = input("Site: "), input("Username / E-Mail: "), \
                                      input("Counter (1): ").strip(" "), input("Length (16): ").strip(" ")
    if site == "": site = "None"
    if username == "": counter = "None@None.None"
    if counter == "" or counter.isdigit() is False: counter = "1"
    if length == "" or length.isdigit() is False: length = "16"
    create_profile(site, username, counter, length)


def add_profiles() -> None:
    while True:
        add_profile()
        print("")
        ask = input("Continue (Y/n): ").lower().strip()
        print("")

        if ask == "n" or ask not in ["y", "n", ""]:
            _list_profiles(info=False)
            break


def remove_profile() -> None:
    _list_profiles()
    _id = _select_profile(only_id=True)
    delete_profile(_id)
    _list_profiles(info=False)


def remove_profiles() -> None:
    _list_profiles(info=False)
    print("\nEnter S.No. Of All Profiles You Want To Remove Seperated By Coma ','")
    print("For Example: > 1, 2, 3, 4")
    print("NOTE: Any Non-Numeric Value Will Terminate The Process")

    ids = []
    try:
        ids = [i if i.isdigit() else int(i) for i in input(f"{get_mode()} > ").replace(" ", "").split(",")]
    except ValueError as e:
        print("\nInvalid Input: ", e)
        exit(1)

    for _id in ids:
        delete_profile(_id)
    _list_profiles(info=False)


def get_password() -> None:
    mp_hash = get_master_password()
    _list_profiles()
    while True:
        profile = _select_profile()
        if profile is None: continue
        passwd = generate_password(profile, mp_hash)
        copy(passwd)
        print("Copied To Clipboard")


def usage() -> None:
    print("""
USAGE: offsync [Options] (add, remove, help)

Optional Arguments:
    add            add new profile
    add c          add multiple profiles at once
     
    remove         remove new profile
    remove c       remove multiple profiles at once
    
    help           Show this help menu
    """)
