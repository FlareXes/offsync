from offsync.storage import save_profile


def create_profile(site, username, salt, length):
    p = {
        '1': {
            "site": site,
            "username": username,
            "salt": salt,
            "length": length
        }
    }
    save_profile(p)
