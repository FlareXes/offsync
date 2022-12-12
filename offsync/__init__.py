import os
from platform import system

USER_HOME_DIR = os.path.expanduser("~")

if system() == "Windows":
    DATABASE_DIR = os.path.join(os.getenv("APPDATA"), "offsync")
elif system() == "Darwin":
    DATABASE_DIR = os.path.join(USER_HOME_DIR, "Library", "Application Support" "offsync")
else:
    DATABASE_DIR = os.path.join(USER_HOME_DIR, ".local", "share", "offsync")

DATABASE = os.path.join(DATABASE_DIR, "profiles.json")

os.makedirs(DATABASE_DIR, exist_ok=True)
