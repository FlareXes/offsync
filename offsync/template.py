from dataclasses import dataclass


@dataclass
class Profile:
    id: str = None,
    site: str = "None"
    username: str = "None"
    counter: str = "1"
    length: str = "16"
