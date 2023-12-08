from utils.table_formats import table_formats
from utils.table_options import table
from rich.console import Console
import subprocess
import typer
import os

console = Console()


def _table_options():
    console.print(table)
    option_number = int(typer.prompt("Whats option you choose?"))

    if option_number == 1:
        _table_formats(option_number)
    elif option_number == 2:
        subprocess.run(["python3", "src/download.py"])
    elif option_number == 3:
        os.abort()


def _table_formats(option_number):
    console.print(table_formats)
    option_filter: int = int(typer.prompt("Audio or video?"))

    if option_number == 1 and option_filter == 1:
        subprocess.run(["python3", "src/filter.py", "--audio"])
        _table_options()
    elif option_number == 1 and option_filter == 2:
        subprocess.run(["python3", "src/filter.py", "--video"])
        _table_options()
