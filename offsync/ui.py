from typing import Any, Dict

from rich.console import Console
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

MODE = "> "


def unpack_dict(**kwargs: Dict[str, str]) -> Any:
    return kwargs.values()


class _Table:
    """
    A helper class for creating and displaying formatted tables for profile data.
    """

    def __init__(self, *, vp: bool = False, qp: bool = False, pp: bool = False):
        """
        Initialize the table with columns and prompt flags.

        Args:
            vp (bool): A flag indicating View Prompt visibility.
            qp (bool): A flag indicating Quit Prompt visibility.
            pp (bool): A flag indicating Password Prompt visibility.
        """

        self.table = Table()
        self.table.add_column("S.No.", justify="center", style="bold magenta", header_style="magenta")
        self.table.add_column("Site", justify="center", style="bold green", header_style="green")
        self.table.add_column("Username / E-Mail", justify="center", style="bold red", header_style="red")
        self.table.add_column("Length", justify="center", style="bold green", header_style="green")
        self.table.add_column("Counter", justify="center", style="bold magenta", header_style="magenta")

        self._vp = vp  # View Prompt
        self._qp = qp  # Quit Prompt
        self._pp = pp  # Password Prompt

    def prompts(self) -> str:
        """
        Generate and return formatted prompt options based on prompt flags.

        Returns:
            str: Formatted prompt options string.
        """

        password_format = "[bold magenta] p  [/bold magenta][bold white]>[/bold white]  [bold]print password[/bold]"
        view_format = "[bold magenta] v  [/bold magenta][bold white]>[/bold white]  [bold]view accounts[/bold]"
        quit_format = "[bold magenta] q  [/bold magenta][bold white]>[/bold white]  [bold]quit[/bold]"

        if self._vp and self._qp and self._pp:
            return view_format + "\t" + password_format + "\n" + quit_format
        if self._vp and self._qp:
            return view_format + "\n" + quit_format
        if self._vp:
            return view_format
        if self._qp:
            return quit_format

    def add_row(self, profile: Dict[int | str, str]) -> None:
        _id, site, username, counter, length = unpack_dict(**profile)
        self.table.add_row(str(_id), site, username, length, counter)

    def tabulate(self) -> None:
        """
        Display the formatted table along with any available prompt options.
        """

        console = Console()
        console.print(self.table)
        prompts = self.prompts()
        if prompts: console.print(prompts)


class Input:
    """
    A collection of methods for user input prompts.
    """

    def __init__(self, text: str = None, default: str | int = None, show_default: bool = True):
        """
        Initialize an Input instance with prompt attributes.

        Args:
            text (str): The prompt text.
            default (str | int): The default value for the input.
            show_default (bool): Whether to show choices in prompt.
        """

        self.text = text
        self.default = default
        self.show_default = show_default

    @property
    def integer(self) -> int:
        return IntPrompt.ask(f"[bold cyan]{self.text}[/bold cyan]", default=self.default,
                             show_default=self.show_default)

    @property
    def string(self) -> str:
        return Prompt.ask(f"[bold cyan]{self.text}[/bold cyan]", default=self.default, show_default=self.show_default)

    @property
    def selection(self) -> str:
        mode = get_mode()
        if mode == "View Mode":
            return Prompt.ask(f"\n[bold green]{mode}[/bold green]").strip()

        elif mode == "Update Mode":
            return Prompt.ask(f"\n[bold yellow]{mode}[/bold yellow]").strip()

        else:
            return Prompt.ask(f"\n[bold red]{mode}[/bold red]").strip()

    @staticmethod
    def getpass(prompt: str) -> str:
        """
        Prompt the user for a password input in a secure manner.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The user-input password.
        """

        ans = Prompt.ask(f"[bold medium_spring_green]{prompt}[/bold medium_spring_green]", password=True, default="",
                         show_default=False)
        return ans


class Print:
    """
    A collection of methods for colored console printing.
    """

    def __init__(self, text: str):
        """
        Initialize a Print instance with text to be printed.

        Args:
            text (str): The text to be printed.
        """

        console = Console()
        console.print(f"[bold]{text}[/bold]")

    @staticmethod
    def success(text: str) -> None:
        console = Console()
        console.print(f"[bold green]{text}[/bold green]")

    @staticmethod
    def warning(text: str) -> None:
        console = Console()
        console.print(f"[bold yellow]{text}[/bold yellow]")

    @staticmethod
    def fail(text: str) -> None:
        console = Console()
        console.print(f"[bold red]{text}[/bold red]")

    @staticmethod
    def info(text: str):
        console = Console()
        console.print(f"[bold cyan]{text}[/bold cyan]")


def set_mode(status: str) -> None:
    global MODE
    MODE = status


def get_mode() -> str:
    return MODE
