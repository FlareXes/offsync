import json
import os.path

from offsync import DATABASE


def load_profiles():
    with open(DATABASE, "r") as f:
        return json.load(f)


def _dump_profiles(profiles):
    with open(DATABASE, "w") as f:
        json.dump(profiles, f, indent=4)


def save_profile(profile):
    profiles = load_profiles()
    total_profiles = len(profiles)
    profile[total_profiles + 1] = profile['1']
    del profile['1']
    profiles.update(profile)
    _dump_profiles(profiles)


def delete_profile(_id):
    profiles = load_profiles()
    del profiles[_id]
    _dump_profiles(profiles)


if not os.path.exists(DATABASE):
    with open(DATABASE, "w") as file:
        json.dump({}, file)
