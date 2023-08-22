import os
from platform import system

USER_HOME_DIR = os.path.expanduser("~")

# Determine the appropriate directory for the database based on the operating system
if system() == "Windows":
    DATABASE_DIR = os.path.join(os.getenv("APPDATA"), "offsync")
elif system() == "Darwin":
    DATABASE_DIR = os.path.join(USER_HOME_DIR, "Library", "Application Support", "offsync")
else:
    DATABASE_DIR = os.path.join(USER_HOME_DIR, ".local", "share", "offsync")

os.makedirs(DATABASE_DIR, exist_ok=True)
DATABASE = os.path.join(DATABASE_DIR, "profiles.sqlite3")

# At this point, the code has determined the appropriate database path based on the user's operating system
# and ensured that the directory structure is in place.
