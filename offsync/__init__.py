import os

USER_HOME_DIR = os.path.expanduser("~")

DATABASE_DIR = os.path.join(USER_HOME_DIR, ".config", "offsync")
DATABASE = os.path.join(DATABASE_DIR, "profiles.json")

os.makedirs(DATABASE_DIR, exist_ok=True)
