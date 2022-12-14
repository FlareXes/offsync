from typing import Any, Dict

from rich.console import Console
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

MODE = ""
TABLE_VIEW_PROMPT = False
TABLE_QUIT_PROMPT = False


def unpack_dict(**kwargs: Dict[str, str]) -> Any:
    return kwargs.values()


class _Table:
    def __init__(self) -> None:
        self.table = Table()
        self.table.add_column("S.No.", justify="center", style="bold magenta", header_style="magenta")
        self.table.add_column("Site", justify="center", style="bold green", header_style="green")
        self.table.add_column("Username / E-Mail", justify="center", style="bold red", header_style="red")
        self.table.add_column("Length", justify="center", style="bold green", header_style="green")
        self.table.add_column("Counter", justify="center", style="bold magenta", header_style="magenta")

    def add_row(self, _id: str, profile: Dict[str, str]) -> None:
        site, username, counter, length = unpack_dict(**profile)
        self.table.add_row(_id, site, username, length, counter)

    def tabulate(self) -> None:
        console = Console()
        console.print(self.table)
        info = get_table_prompt()
        if info is not None: console.print(info)


class Input:
    def __init__(self, text: str = None, default: str | int = None, show_default: bool = True):
        self.text = text
        self.default = default
        self.show_default = show_default

    @property
    def integer(self):
        return IntPrompt.ask(f"[bold cyan]{self.text}[/bold cyan]", default=self.default,
                             show_default=self.show_default)

    @property
    def string(self):
        return Prompt.ask(f"[bold cyan]{self.text}[/bold cyan]", default=self.default, show_default=self.show_default)

    @property
    def selection(self):
        mode = get_mode()
        if mode == "View Mode":
            return Prompt.ask(f"\n[bold green]{mode}[/bold green]").strip()

        elif mode == "Update Mode":
            return Prompt.ask(f"\n[bold yellow]{mode}[/bold yellow]").strip()

        else:
            return Prompt.ask(f"\n[bold red]{mode}[/bold red]").strip()

    @staticmethod
    def getpass(prompt: str) -> str:
        ans = Prompt.ask(f"[bold medium_spring_green]{prompt}[/bold medium_spring_green]", password=True,
                         default="", show_default=False)
        return ans


class Print:
    def __init__(self, text: str = None):
        console = Console()
        console.print(f"[bold]{text}[/bold]")

    @staticmethod
    def success(text):
        console = Console()
        console.print(f"[bold green]{text}[/bold green]")

    @staticmethod
    def warning(text):
        console = Console()
        console.print(f"[bold yellow]{text}[/bold yellow]")

    @staticmethod
    def fail(text):
        console = Console()
        console.print(f"[bold red]{text}[/bold red]")

    @staticmethod
    def info(text):
        console = Console()
        console.print(f"[bold cyan]{text}[/bold cyan]")


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
    view_format = "[bold magenta] v [/bold magenta][bold white] > [/bold white] [bold]view profiles[/bold]"
    quit_format = "[bold magenta] q [/bold magenta][bold white] > [/bold white] [bold]quit[/bold]"

    if TABLE_VIEW_PROMPT and TABLE_QUIT_PROMPT:
        return view_format + "\n" + quit_format

    if TABLE_VIEW_PROMPT:
        return view_format

    if TABLE_QUIT_PROMPT:
        return quit_format

    return None
