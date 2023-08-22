import sqlite3
from typing import List, Iterator, Tuple

from offsync import DATABASE
from offsync.template import Profile


class Database:
    """
    Manages interactions with the SQLite database for CRUDing user profiles.

    Attributes:
        conn (sqlite3.Connection): SQLite database connection.
        cursor (sqlite3.Cursor): SQLite database cursor.
    """

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """
        Destructor to close the database connection when the object is destroyed.
        """

        self.conn.close()

    def init_database(self) -> None:
        """
        Initialize the database by creating the necessary table if it doesn't exist.
        """

        account_table_schema = """
        CREATE TABLE IF NOT EXISTS Profiles
        (id              INTEGER     PRIMARY KEY,
         site            TEXT        NOT NULL,
         username        TEXT        NOT NULL,
         counter         TEXT        NOT NULL,
         length          TEXT        NOT NULL);
        """

        self.cursor.execute(account_table_schema)
        self.conn.commit()

    def create(self, profile_values: List) -> None:
        """
        Insert a new profile entry into the database.

        Args:
            profile_values (List): Values for the profile fields (site, username, counter, length).
        """

        query = """INSERT INTO Profiles (site, username, counter, length) VALUES (?, ?, ?, ?)"""
        self.cursor.execute(query, profile_values)
        self.conn.commit()

    def read(self) -> List[Tuple]:
        """
        Retrieve all profiles from the database.

        Returns:
            List[Tuple]: List of profile entries as tuples.
        """

        query = """SELECT * FROM Profiles"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, profile: Profile) -> None:
        """
        Update an existing profile entry in the database.

        Args:
            profile (Profile): The updated profile information.
        """

        query = """UPDATE Profiles SET site = ?, username = ?, counter = ?, length = ? WHERE id = ?"""

        values = (profile.site, profile.username, profile.counter, profile.length, profile._id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete(self, profile_id: str) -> None:
        """
        Delete a profile entry from the database.

        Args:
            profile_id (str): The ID of the profile to be deleted.
        """

        account_query = """DELETE FROM Profiles WHERE id = ?"""
        self.cursor.execute(account_query, profile_id)
        self.conn.commit()

    def select_by_id(self, profile_id: str) -> Tuple:
        """
        Retrieve a profile entry from the database by its ID.

        Args:
            profile_id (str): The ID of the profile to be retrieved.

        Returns:
            Tuple: Profile information as a tuple.
        """

        query = """SELECT * FROM Profiles WHERE id = ?"""
        self.cursor.execute(query, profile_id)
        return self.cursor.fetchone()


def profiles() -> Iterator[Profile]:
    """
    Retrieve profiles from the database and yield Profile instances.

    Yields:
        Profile: Profile instances retrieved from the database.
    """

    try:
        raw_profiles = Database().read()
        for raw_profile in raw_profiles:
            yield Profile(*raw_profile)
    except Exception as e:
        print("Error at DEF profiles:", e)


def create_profile(profile: Profile) -> None:
    try:
        Database().create(list(profile.__dict__.values())[1:])
    except Exception as e:
        print("Error at DEF create_profile:", e)


def delete_profile(_id: str) -> None:
    Database().delete(_id)


def update_profile(new_profile: Profile) -> None:
    db = Database()
    original_profile = Profile(*db.select_by_id(str(new_profile._id)))

    if new_profile.site is not None:
        original_profile.site = new_profile.site

    if new_profile.username is not None:
        original_profile.username = new_profile.username

    if new_profile.counter is not None:
        original_profile.counter = new_profile.counter

    if new_profile.length is not None:
        original_profile.length = new_profile.length

    db.update(original_profile)
