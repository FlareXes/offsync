import os
from platform import system

USER_HOME_DIR = os.path.expanduser("~")

if system() == "Windows":
    DATABASE_DIR = os.path.join(os.getenv("APPDATA"), "watodo")
elif system() == "Darwin":
    DATABASE_DIR = os.path.join(USER_HOME_DIR, "Library", "Application Support" "watodo")
else:
    DATABASE_DIR = os.path.join(USER_HOME_DIR, ".local", "share", "watodo")

DATABASE = os.path.join(DATABASE_DIR, "profiles.json")

os.makedirs(DATABASE_DIR, exist_ok=True)
