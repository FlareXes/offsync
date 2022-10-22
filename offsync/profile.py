from offsync.storage import save_profile


def create_profile(site, username, counter, length):
    p = {
        '1': {
            "site": site,
            "username": username,
            "counter": counter,
            "length": length
        }
    }
    save_profile(p)
