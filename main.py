from utils.table_options import table
from rich.console import Console
from rich import print
import subprocess

console = Console()


if __name__ == "__main__":
    console.print(table)
    print("[orange3] Whats option you choose?")
    option_number: int = int(input("» "))
    print("[orange3] Audio or video?")
    option_filter: str = input("» ")
    if option_number == 1 and option_filter == "audio": subprocess.run(["python3", "scripts/filter.py", "--audio"])
