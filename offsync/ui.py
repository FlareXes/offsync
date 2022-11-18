from typing import Any, Dict

from rich.console import Console
from rich.table import Table

MODE = ""
TABLE_VIEW_PROMPT = False
TABLE_QUIT_PROMPT = False


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

    def tabulate(self) -> None:
        console = Console()
        console.print(self.table)
        info = get_table_prompt()
        if info is not None: console.print(info)


def set_mode(status: str) -> None:
    global MODE
    MODE = status


def get_mode() -> str:
    return MODE


def set_table_prompts(v: bool = False, q: bool = False):
    global TABLE_VIEW_PROMPT
    global TABLE_QUIT_PROMPT

    TABLE_VIEW_PROMPT = v
    TABLE_QUIT_PROMPT = q


def get_table_prompt() -> str | None:
    view_format = "[magenta] v [/ magenta][bold white] > [/bold white] view profiles"
    quit_format = "[magenta] q [/ magenta][bold white] > [/bold white] quit"

    if TABLE_VIEW_PROMPT and TABLE_QUIT_PROMPT:
        return view_format + "\n" + quit_format

    if TABLE_VIEW_PROMPT:
        return view_format

    if TABLE_QUIT_PROMPT:
        return quit_format

    return None
