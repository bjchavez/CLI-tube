from rich.console import Console
from rich.table import Table
from rich import box

table_formats = Table(title="Formats", show_lines=True, box=box.ROUNDED)

table_formats.add_column("Option", justify="center", style="orange3")
table_formats.add_column("Description", justify="left")

table_formats.add_row("1", "For filter to audio.")
table_formats.add_row("2", "For filter to video.")

console = Console()


if __name__ == "__main__":
    console.print(table_formats)
