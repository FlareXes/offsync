import hashlib

COST_FACTOR = 2 ** 14
ROUND = 8
PARALLEL_FACTOR = 1
KEY_LENGTH = 32  # bytes


def kdf_scrypt(master_password: str, salt: str):
    password, salt = master_password.encode("utf-8"), salt.encode("utf-8")
    key = hashlib.scrypt(password, salt=salt, n=COST_FACTOR, r=ROUND, p=PARALLEL_FACTOR, dklen=KEY_LENGTH)
    return key
