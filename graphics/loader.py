from pathlib import Path
from menus.render import draw_box
from utils.screen import clear_area
from utils.storage import read_json, read_txt

def print_art(art, clear=True, box=False):
    """Prints the specified art.

    Args:
        art (str): The name of the art to print.
    """
    data = read_json(Path('graphics/arts.json'))

    if art in data:
        art_data = read_txt(data[art]['path'])
        art_lines = art_data.split('\n')

        x, y = data[art]['position']
        height, width = data[art]['dimension']

        if clear:
            clear_area(x, y, width, height)
        if box:
            clear_area(x-3, y-3, width+6, height+6)
            draw_box(x-2, y-2, width+3, height+3)

        for line in art_lines:
            print("\x1b[" + str(y) + ";" + str(x) + "H" + line)
            y += 1
