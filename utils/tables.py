from utils.table_formats import table_formats
from utils.table_options import table
from rich.console import Console
from rich import print
import subprocess
import os

console = Console()


def _table_options():
    console.print(table)
    print("[orange3] Whats option you choose?")
    option_number: int = int(input("» "))
    if option_number == 3:
        os.abort()
    _table_formats(option_number)


def _table_formats(option_number):
    console.print(table_formats)
    print("[orange3] Audio or video?")
    option_filter: int = int(input("» "))

    if option_number == 1 and option_filter == 1:
        subprocess.run(["python3", "src/filter.py", "--audio"])
        _table_options()
    elif option_number == 1 and option_filter == 2:
        subprocess.run(["python3", "src/filter.py", "--video"])
        _table_options()

