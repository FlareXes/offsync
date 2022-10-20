import random
import string

from offsync.security import kdf_scrypt

CHAR_ARRAY = string.ascii_letters + string.digits + string.punctuation


def _calc_seed(profile, master_password):
    salt = profile["site"] + profile["username"] + profile["salt"] + profile["length"]
    hex_entropy = kdf_scrypt(master_password, salt).hex()
    return int(hex_entropy, 16)


def generate_password(profile, master_password):
    seed = _calc_seed(profile, master_password)
    random.seed(seed)
    return "".join(random.choice(CHAR_ARRAY) for i in range(int(profile["length"])))

