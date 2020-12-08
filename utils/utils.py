# Common class to group useful stuff I do multiple times

import os
import requests

def get_input(year: str, day: str) -> str:
    filename = file = os.path.join(os.path.dirname(__file__), '..', year, day, 'input.txt')
    try:
        with open(filename, 'r+') as file:
            return file.read().strip()
    except:
        with open(filename, 'w+') as file:
            session = os.environ['AOC_SESSION']
            lines = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=dict(session=session)).text.strip()
            file.write(lines)
            return lines