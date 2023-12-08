from pytube import YouTube
from rich import print
import typer

filter_app = typer.Typer()


@filter_app.command()
def filter(audio: bool = False, video: bool = False):
    link: str = typer.prompt("Link to filter")
    y_link = YouTube(link)

    if audio:
        y_filter = y_link.streams.filter(only_audio=True)
        for f in y_filter:
            print(f, end="\n")
    elif video:
        y_filter = y_link.streams.filter(only_video=True)
        for f in y_filter:
            print(f, end="\n")


if __name__ == "__main__":
    filter_app()
