from inputs.input_handler import getkey, get_key_change
from utils.screen import clear_area
from .render import render_menu, display_tooltip

close = False

def close_menu():
    global close
    close = True

def exit_game():
    globals.settings.update({"loop": False})

def update_option(current_option, change, total_options):
    return (current_option + change) % total_options

def display_menu(options, rows, cols, x=2, y=2, box_width=15):
    current_option = 0
    total_options = len(options)
    page_start = 0
    items_per_page = rows * cols

    global close
    while True:
        render_menu(options, current_option, rows, cols, x, y, box_width, page_start)
        display_tooltip(options[current_option][2])
        key = getkey()

        if key == b' ':
            options[current_option][1]()
        if key == b'q' or close:
            close = False
            clear_area(x, y, rows * 3 + 1, cols * (box_width + 1) + 1)
            return

        change = get_key_change(key, rows, cols)
        current_option = update_option(current_option, change, total_options)

        if current_option < page_start:
            page_start = max(0, current_option - (current_option % items_per_page))
        elif current_option >= page_start + items_per_page:
            page_start = current_option - (current_option % items_per_page)
