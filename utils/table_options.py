from rich.console import Console
from rich.table import Table

table = Table(title="Ty-Tube", show_lines=True)

table.add_column("#", justify="center", style="orange3")
table.add_column("Option", justify="left", style="green")
table.add_column("Description", justify="left")

table.add_row("1", "Filter", "This option filters a link from Youtube, you can choose between audio or video.")
table.add_row("2", "Download", "This option downloads a audio or video from Youtube.")

console = Console()


if __name__ == "__main__":
    console.print(table)
