import sys
from typing import Dict

from offsync.clipboard import copy
from offsync.password import generate_password
from offsync.profile import create_profile
from offsync.security import get_master_password
from offsync.storage import load_profiles, delete_profile, update_profile
from offsync.ui import _Table, set_table_prompts, Input, Print


def list_profiles() -> None:
    table = _Table()
    profiles = load_profiles().items()

    for _id, profile in profiles: table.add_row(_id, profile)

    if len(profiles) == 0:
        table.tabulate()
        sys.exit(0)

    table.tabulate()


def select_profile(only_id: bool = False) -> Dict[str, str] | str | None:
    ask = Input().selection

    if ask == "q" or ask == "quit" or ask == "exit":
        copy("")
        sys.exit(0)

    if only_id:
        return ask

    if ask == "v" or ask == "view":
        list_profiles()
        return None

    try:
        return load_profiles()[ask]
    except KeyError:
        Print.fail("Invalid Input!")
        return None


def add_profile() -> None:
    site = Input("Site", default="None").string
    username = Input("Username / E-Mail", default="None").string
    counter = str(Input("Counter", default=1).integer)
    length = str(Input("Length", default=16).integer)

    create_profile(site, username, counter, length)


def add_profiles() -> None:
    set_table_prompts(v=False, q=False)
    while True:
        add_profile()
        print("")  # TODO: CHeck It
        ask = input("Continue (Y/n): ").lower().strip()
        print("")

        if ask == "n" or ask not in ["y", "n", ""]:
            list_profiles()
            break


def remove_profile() -> None:
    set_table_prompts(q=True)
    list_profiles()
    _id = select_profile(only_id=True)
    delete_profile(_id)
    set_table_prompts(v=False, q=False)
    list_profiles()


def remove_profiles() -> None:
    set_table_prompts(v=False, q=False)
    list_profiles()
    Print.warning("\nEnter S.No. Of All Profiles You Want To Remove Separated By Coma ','")
    Print.warning("For Example: > 1, 2, 3, 4")
    Print.fail("Note: Any Non-Numeric Value Will Terminate The Process")

    ids = []
    try:
        ids = [i if i.isdigit() else int(i) for i in Input("").string.replace(" ", "").split(",")]
    except ValueError as e:
        Print.fail(f"\nInvalid Input: {e}")
        exit(1)

    for _id in ids:
        delete_profile(_id)
    list_profiles()


def get_password(prompt: bool = False) -> None:
    set_table_prompts(v=True, q=True)
    mp_hash = get_master_password()
    list_profiles()
    while True:
        profile = select_profile()
        if profile is None: continue
        passwd = generate_password(profile, mp_hash)
        copy(passwd)
        if prompt: print(passwd)
        Print.info("Copied To Clipboard")


def change_password() -> None:
    set_table_prompts(q=True)
    list_profiles()
    _id = select_profile(only_id=True)
    if _id == "" or _id.isdigit() is False: sys.exit(2)
    Print.warning("> Leave field empty if you don't want to change something\n")

    site = Input("Site").string
    username = Input("Username / E-Mail").string
    counter = Input("Counter").integer
    length = Input("Length").integer

    if counter is not None:
        counter = str(counter)
    if length is not None:
        length = str(length)

    update_profile(_id, site, username, counter, length)
    set_table_prompts(v=False, q=False)
    list_profiles()


def usage() -> None:
    print("""
USAGE: offsync [Options] (add, remove, help)

Optional Arguments:
    add            add new profile
    add c          add multiple profiles at once
     
    remove         remove new profile
    remove c       remove multiple profiles at once
   
    update         change profile counter to update password
    prompt         show password in clear text
    help           Show this help menu
    """)
