import hashlib
import random
import string

from offsync.template import Profile
from offsync.ui import Input

COST_FACTOR = 2 ** 14
ROUND = 8
PARALLEL_FACTOR = 1
KEY_LENGTH = 32  # bytes
CHAR_ARRAY = string.ascii_letters + string.digits + string.punctuation


def _kdf_scrypt(password: str, salt: str) -> bytes:
    _password, _salt = password.encode("utf-8"), salt.encode("utf-8")
    key = hashlib.scrypt(password=_password, salt=_salt, n=COST_FACTOR, r=ROUND, p=PARALLEL_FACTOR, dklen=KEY_LENGTH)
    return key


def _calc_seed(profile: Profile, master_password_hash: str) -> int:
    salt = profile.site + profile.username + profile.counter + profile.length
    hex_entropy = _kdf_scrypt(master_password_hash, salt).hex()
    return int(hex_entropy, 16)


def generate_profile_password(profile: Profile, master_password_hash: str) -> str:
    seed = _calc_seed(profile, master_password_hash)
    random.seed(seed)
    return "".join(random.choice(CHAR_ARRAY) for i in range(int(profile.length)))


def get_master_password() -> str:
    return hashlib.sha512(Input.getpass("Secret Key").encode("utf-8")).hexdigest()
