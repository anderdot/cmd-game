from pathlib import Path
from utils.storage import read_json, read_txt

def print_art(art):
    """Prints the specified art.

    Args:
        art (str): The name of the art to print.
    """
    art = art.lower()
    data = read_json(Path('graphics/arts.json'))

    if art in data:
        art_data = read_txt(data[art]['path'])
        art_lines = art_data.split('\n')

        x, y = data[art]['position']
        for line in art_lines:
            print("\x1b[" + str(y) + ";" + str(x) + "H" + line)
            y += 1
