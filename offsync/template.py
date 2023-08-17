from dataclasses import dataclass


@dataclass
class Profile:
    _id: int = None,
    site: str = "None"
    username: str = "None"
    counter: str = "1"
    length: str = "16"
