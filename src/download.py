from pytube import YouTube
from rich import print
from pathlib import Path
import typer
import os

download_app = typer.Typer()


@download_app.command()
def download():
    print("[orange3] Link to download: ")
    link: str = input("» ")
    print("[orange3] Itag: ")
    itag: int = int(input("» "))

    youtube_link = YouTube(link)
    stream = youtube_link.streams.get_by_itag(itag)
    if stream is not None:
        root_path = Path.home()
        str_path = "download_all"
        path = Path(f"{root_path}/{str_path}")
        if path.is_dir():
            stream.download(f"/{path}")
        else:
            folder_path = os.mkdir(f"{path}")
            stream.download(f"/{folder_path}")


if __name__ == "__main__":
    download_app()
