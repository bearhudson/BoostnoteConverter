#!/usr/bin/python3

import json
from rich.console import Console
from rich.markdown import Markdown
import os


console = Console()
path = input("Please enter the file path: ")
try:
    files = os.scandir(path)
    for file in files:
        with open(file, 'r') as json_file:
            print(f"\n\nReading: {file.name}")
            json_data = json.load(json_file)
            with open(f"output/{file.name}.txt", 'x') as new_file:
                try:
                    console.print(Markdown(json_data['title']))
                    new_file.write(json_data['title'])
                    console.print(Markdown(json_data['content']))
                    new_file.write(json_data['content'])
                except KeyError:
                    pass
                new_file.close()
except FileNotFoundError as error:
    print(f"Folder: {error.filename} not found. Please try again.")
