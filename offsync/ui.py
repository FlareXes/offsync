from typing import Any, Dict

from rich.console import Console
from rich.table import Table

MODE = ""


def unpack_dict(**kwargs: Dict[str, str]) -> Any:
    return kwargs.values()


class _Table:
    def __init__(self) -> None:
        self.table = Table()
        self.table.add_column("S.No.", justify="center", style="magenta", header_style="magenta")
        self.table.add_column("Site", justify="center", style="green", header_style="green")
        self.table.add_column("Username / E-Mail", justify="center", style="red", header_style="red")
        self.table.add_column("Length", justify="center", style="green", header_style="green")
        self.table.add_column("Counter", justify="center", style="magenta", header_style="magenta")

    def add_row(self, _id: str, profile: Dict[str, str]) -> None:
        site, username, counter, length = unpack_dict(**profile)
        self.table.add_row(_id, site, username, length, counter)

    def tabulate(self, info: bool = True) -> None:
        console = Console()
        console.print(self.table)
        if info:
            info_format = "[magenta] v [/ magenta][bold white] > [/bold white] view profiles" \
                          + "\n" \
                          + "[magenta] q [/ magenta][bold white] > [/bold white] quit"

            console.print(info_format)


def set_mode(status: str) -> None:
    global MODE
    MODE = status


def get_mode() -> str:
    return MODE
