import hashlib
from getpass import getpass

COST_FACTOR = 2 ** 14
ROUND = 8
PARALLEL_FACTOR = 1
KEY_LENGTH = 32  # bytes


def kdf_scrypt(password: str, salt: str) -> bytes:
    _password, _salt = password.encode("utf-8"), salt.encode("utf-8")
    key = hashlib.scrypt(password=_password, salt=_salt, n=COST_FACTOR, r=ROUND, p=PARALLEL_FACTOR, dklen=KEY_LENGTH)
    return key


def get_master_password() -> str:
    return hashlib.sha512(getpass("Secret Key: ").encode("utf-8")).hexdigest()
