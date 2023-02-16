from hashlib import sha1
from urllib.request import Request, urlopen

from offsync.password import generate_password
from offsync.storage import load_profiles


class HaveIBeenPwned:
    def __init__(self, mp_hash):
        self.mp_hash = mp_hash

    def _get_profiles(self):
        profiles = load_profiles()
        for profile_id in profiles:
            p = generate_password(profiles[profile_id], self.mp_hash)
            p_hash = sha1(p.encode("UTF-8")).hexdigest().upper()
            profiles[profile_id]["prefix"] = p_hash[:5]
            profiles[profile_id]["suffix"] = p_hash[5:]
        return profiles

    def is_pwned(self):
        profiles = self._get_profiles()
        pwned_id = []

        for profile_id in profiles:
            prefix = profiles[profile_id]["prefix"]
            suffix = profiles[profile_id]["suffix"]

            # Get all suffixes respective to given prefix
            request = Request(f"https://api.pwnedpasswords.com/range/{prefix}")
            request.add_header("Add-Padding", "true")
            with urlopen(request) as breached_hashes:
                breached_suffixes = [items.decode("utf-8").split(":")[0] for items in breached_hashes.read().split()]

            # Check if suffix is already present in breached suffixes
            if suffix in breached_suffixes:
                pwned_id.append(profile_id)

        return pwned_id
