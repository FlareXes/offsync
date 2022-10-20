from getpass import getpass
from hashlib import sha512

from offsync.password import generate_password
from offsync.profile import create_profile
from offsync.storage import _load_profiles
from offsync.ui import _Table


def _list_profiles():
    table = _Table()
    for _id, profile in _load_profiles().items(): table.add_row(_id, profile)
    table.tabulate()


def get_password():
    _list_profiles()
    master_passwd = sha512(getpass("Secret Key: ").encode("utf-8")).hexdigest()
    while True:
        ask = input("\n> ")
        try:
            profile = _load_profiles()[ask]
        except KeyError as e:
            print("Invalid Input!")
            continue
        passwd = generate_password(profile, master_passwd)
        print(passwd)


def add_profile():
    site, username, salt, length = input("Site: "), input("Username / E-Mail: "), input("Salt: "), input("Length: ")
    if length.strip(" ") == "": length = 16
    create_profile(site, username, salt, length)
