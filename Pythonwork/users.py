# SAVING AND READIGN USER-GENERATED DATA

from pathlib import Path
import json

username = input("What is your name? ")
path = Path('username.json') # Decide location and name of the file

contents = json.dumps(username) # Turn in into a string?
path.write_text(contents) # Write contents to it

print(f"We'll remember you when you come back, {username}!")

