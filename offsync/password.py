import random
import string
from typing import Dict

from offsync.security import kdf_scrypt

CHAR_ARRAY = string.ascii_letters + string.digits + string.punctuation


def _calc_seed(profile: Dict[str, str], master_password_hash: str) -> int:
    salt = profile["site"] + profile["username"] + profile["counter"] + profile["length"]
    hex_entropy = kdf_scrypt(master_password_hash, salt).hex()
    return int(hex_entropy, 16)


def generate_password(profile: Dict[str, str], master_password_hash: str) -> str:
    seed = _calc_seed(profile, master_password_hash)
    random.seed(seed)
    return "".join(random.choice(CHAR_ARRAY) for i in range(int(profile["length"])))
