from rich.console import Console
from rich.table import Table


def unpack_dict(**kwargs):
    return kwargs.values()


class _Table:
    def __init__(self):
        self.table = Table()
        self.table.add_column("Profiles", justify="center", style="cyan", no_wrap=True, header_style="white")
        # self.table.add_column("Site", justify="left", style="cyan", no_wrap=True, header_style="white")
        # self.table.add_column("Username / E-Mail", justify="left", style="cyan", no_wrap=True, header_style="white")
        # self.table.add_column("Salt", justify="left", style="cyan", no_wrap=True, header_style="white")
        # self.table.add_column("Length", justify="left", style="cyan", no_wrap=True, header_style="white")

    def add_row(self, _id, profile):
        # self.table.add_row(f"[magenta]{str(i + 1)}[/ magenta] [bold white]>[/bold white] {todo}")
        site, username, salt, length = unpack_dict(**profile)
        row_format = f"{_id} > {site} > {username} > {salt} > {length}"
        self.table.add_row(row_format)

    def tabulate(self):
        console = Console()
        console.print(self.table)
