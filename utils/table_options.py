from rich.console import Console
from rich.table import Table
from rich import box

table = Table(title="Ty-Tube", show_lines=True, box=box.ROUNDED)

table.add_column("Option", justify="center", style="orange3")
table.add_column("Description", justify="left")

table.add_row("1", "Filters a link from Youtube, you can choose between audio or video.")
table.add_row("2", "Downloads a audio or video from Youtube.")
table.add_row("3", "Exit app.")

console = Console()


if __name__ == "__main__":
    console.print(table)
