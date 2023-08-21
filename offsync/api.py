from hashlib import sha1
from typing import Dict, List, Iterator
from urllib.request import Request, urlopen

from offsync.security import get_master_password, generate_profile_password
from offsync.storage import profiles
from offsync.ui import Print


class HaveIBeenPwned:
    def __init__(self):
        self.mp_hash = get_master_password()

    @staticmethod
    def is_pwned(config: Dict) -> bool:
        request = Request(f"https://api.pwnedpasswords.com/range/{config.get('prefix')}")
        request.add_header("Add-Padding", "true")

        with urlopen(request) as breached_hashes:
            breached_suffixes = [items.decode("utf-8").split(":")[0] for items in breached_hashes.read().split()]

        if config.get("suffix") in breached_suffixes:
            return True

        return False

    def profiles_config(self) -> Iterator[Dict[str, str]]:
        for profile in profiles():
            p_hash = sha1(generate_profile_password(profile, self.mp_hash).encode("UTF-8")).hexdigest().upper()
            yield {
                "id": profile._id,
                "prefix": p_hash[:5],
                "suffix": p_hash[5:],
            }

    def get_pwned_profile_ids(self) -> List[str | None]:
        Print.warning("Checking For Breached Generated Profile Passwords...")

        pwned_password_ids = []
        for config in self.profiles_config():
            if self.is_pwned(config):
                pwned_password_ids.append(config.get("id"))
        return pwned_password_ids
