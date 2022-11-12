from offsync.storage import save_profile


def create_profile(site: str, username: str, counter: str, length: str) -> None:
    p = {
        '1': {
            "site": site,
            "username": username,
            "counter": counter,
            "length": length
        }
    }
    save_profile(p)
