from pytube import YouTube
from pathlib import Path
import typer
import os

download_app = typer.Typer()


@download_app.command()
def download():
    link = typer.prompt(typer.style("Link to download", fg=typer.colors.RED))
    itag = int(typer.prompt(typer.style("Itag", fg=typer.colors.RED)))

    download_path = "clitube_⏩"
    youtube_link = YouTube(link)
    stream = youtube_link.streams.get_by_itag(itag)

    if stream is not None:
        root_path = Path.home()
        path = Path(f"{root_path}/{download_path}")

        if path.is_dir():
            stream.download(f"/{path}")
        else:
            folder_path = os.mkdir(f"{path}")
            stream.download(f"/{folder_path}")


if __name__ == "__main__":
    download_app()
