from utils.cursor import move_cursor
from utils.screen import clear_area
from .scroll import render_scroll_bar

def render_option(option_text, selected, cursor_x, cursor_y, box_width):
    if selected:
        move_cursor(cursor_x, cursor_y)
        print(f"╔{'═' * (box_width - 2)}╗")
        move_cursor(cursor_x, cursor_y + 1)
        centered_text = f" {option_text} ".center(box_width - 2)
        print(f"║{centered_text}║")
        move_cursor(cursor_x, cursor_y + 2)
        print(f"╚{'═' * (box_width - 2)}╝")
    else:
        centered_text = f" {option_text} ".center(box_width - 2)
        move_cursor(cursor_x, cursor_y + 1)
        print(f" {centered_text} ")

def render_menu(options, current_option, rows, cols, x, y, box_width, page_start):
    clear_area(x, y, rows * 3 + 1, cols * (box_width + 1) + 2)
    total_options = len(options)
    items_per_page = rows * cols

    for row in range(rows):
        for col in range(cols):
            index = page_start + row * cols + col
            if index < total_options:
                cursor_x = x + col * (box_width + 1)
                cursor_y = y + row * 3
                render_option(options[index][0], index == current_option, cursor_x, cursor_y, box_width)

    if total_options > items_per_page:
        render_scroll_bar(total_options, items_per_page, current_option, rows, cols, x, y, box_width)

def display_tooltip(tooltip, x=2, y=49):
    clear_area(1, y, 1, 150)
    move_cursor(x, y)
    print(f"{tooltip}")
