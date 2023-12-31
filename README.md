# CLI-tube

CLI App to download audio or video from Youtube. :smile:

## Installation Guide

- Clone this repository.
- Create a virtual environment:

  ```console
  $ python3 -m venv .env
  ```
- Activate .env

  ```console
  $ source .env/bin/activate
  ```
- Install requirements.txt file.

  ```console
  $ pip install -r requirements.txt
  ```
- Then, run:

  ```console
  $ ./main.py
  ```

## Usage

You can find its guideline [here](/docs/usage.md).

## What technologies am I using?

- [Typer](https://typer.tiangolo.com/) - Typer, build great CLIs. Easy to code. Based on Python type hints.
- [Pytube](https://pytube.io/en/latest/) - Pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.
- [Rich](https://github.com/Textualize/rich) - Rich is a Python library for rich text and beautiful formatting in the terminal.

## To-do

- [ ] There is an issue right now with video downloads. I can't find a way to download videos with audio, so it's somenthing I need to
figure out.
