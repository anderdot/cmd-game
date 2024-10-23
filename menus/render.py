from utils.cursor import move_cursor
from utils.screen import clear_area
from .scroll import render_scroll_bar
from locales.translation import get_translated_text, get_size_text

def render_option(option_text, selected, cursor_x, cursor_y, box_width):
    """Renders an option in the menu with a box around it.

    Args:
        option_text (str): The text of the option.
        selected (bool): Whether the option is selected or not.
        cursor_x (int): The x position of the cursor.
        cursor_y (int): The y position of the cursor.
        box_width (int): The width of the option box.
    """
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
    """Renders the menu with scrolling functionality.

    Args:
        options (list): A list of tuples containing the option text and a callback function.
        current_option (int): The index of the currently selected option.
        rows (int): The number of rows visible in the menu.
        cols (int): The number of columns visible in the menu.
        x (int): The x position for the menu.
        y (int): The y position for the menu.
        box_width (int): The width of each option box.
        page_start (int): The starting index of the current page of options.
    """
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

def display_tooltip(key_tooltip, x=2, y=49):
    """Displays the translated tooltip at the given coordinates (x, y).

    Args:
        key_tooltip (str): The key for the translated tooltip.
        x (int, optional): The x position for the tooltip. Defaults to 2.
        y (int, optional): The y position for the tooltip. Defaults to 49.
    """
    tooltip = get_translated_text(key_tooltip)
    clear_area(1, y, 1, 150)
    move_cursor(x, y)
    print(f"{tooltip}")

def display_title(key_text, x, y):
    """Displays the translated title at the given coordinates (x, y).

    Args:
        key_text (str): The key for the translated text.
        x (int): The x position for the title.
        y (int): The y position for the title.
    """
    translated_text, size = get_translated_text(key_text)
    box_width = size + 4
    clear_area(x, y, 3, box_width)
    move_cursor(x, y)
    print(f"┌{'─' * (box_width - 2)}┐")
    move_cursor(x, y + 1)
    print(f"┼ {translated_text} ┼")
    move_cursor(x, y + 2)
    print(f"└{'─' * (box_width - 2)}┘")

def draw_box(x, y, width, height):
    """Draws a box with the given width and height at position (x, y), leaving the middle empty.

    Args:
        x (int): The x position for the box.
        y (int): The y position for the box.
        width (int): The width of the box.
        height (int): The height of the box.
    """
    clear_area(x, y, height, width)
    move_cursor(x, y)
    print(f"┌{'─' * (width - 2)}┐")

    for i in range(1, height - 1):
        move_cursor(x, y + i)
        print("│", end="")
        move_cursor(x + width - 1, y + i)
        print("│")

    move_cursor(x, y + height - 1)
    print(f"└{'─' * (width - 2)}┘")

def display_title_box(key_text, x, y, width, height, alignment='center'):
    """Draws a box at (x, y) with specified width and height, and displays the translated title inside it.

    Args:
        key_text (str): The key for the translated text.
        x (int): The x position for the box.
        y (int): The y position for the box.
        width (int): The width of the box.
        height (int): The height of the box.
        alignment (str, optional): The text alignment ('left', 'center', 'right'). Defaults to 'center'.
    """
    draw_box(x, y, width, height)

    size = get_size_text(key_text)

    if alignment == 'center':
        title_x = x + (width - size) // 2 - 1
    elif alignment == 'right':
        title_x = x + width - size - 6
    elif alignment == 'left':
        title_x = x + 2

    display_title(key_text, title_x, y - 1)
