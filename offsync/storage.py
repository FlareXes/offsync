import json
import os.path
from typing import Dict

from offsync import DATABASE


def load_profiles() -> Dict[str, Dict[str, str]]:
    with open(DATABASE, "r") as f:
        return json.load(f)


def _dump_profiles(profiles: Dict[str, Dict[str, str]]) -> None:
    with open(DATABASE, "w") as f:
        json.dump(profiles, f, indent=4)


# TODO: WORK ON THIS [save_profile] - Priority: 2
def save_profile(profile: Dict[str, Dict[str, str]]) -> None:
    profiles = load_profiles()
    if len(profiles) > 0:
        max_id = max(map(int, profiles.keys()))
    else:
        max_id = 0
    profile[str(max_id + 1)] = profile['1']
    if len(profile) > 1: del profile['1']
    profiles.update(profile)
    _dump_profiles(profiles)


def delete_profile(_id: str) -> None:
    profiles = load_profiles()
    try:
        del profiles[_id]
    except KeyError:
        pass
    _dump_profiles(profiles)


if not os.path.exists(DATABASE):
    with open(DATABASE, "w") as file:
        json.dump({}, file)
