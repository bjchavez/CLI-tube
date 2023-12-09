from pytube import YouTube
from rich import print
import typer

filter_app = typer.Typer()


@filter_app.command()
def filter(audio: bool = False, video: bool = False):
    enter_link = typer.prompt(typer.style("Link to filter", fg=typer.colors.RED))
    youtube_link = YouTube(enter_link)

    if audio:
        y_filter = youtube_link.streams.filter(only_audio=True)
        for f in y_filter:
            print(f, end="\n")
    elif video:
        y_filter = youtube_link.streams.filter(only_video=True)
        for f in y_filter:
            print(f, end="\n")


if __name__ == "__main__":
    filter_app()
