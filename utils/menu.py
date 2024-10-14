import msvcrt
from utils.colors import Color, print_color
from utils.cursor import hide_cursor, show_cursor, move_cursor

BOX_WIDTH = 41
SELECTED_COLOR = Color.yellow
SELECTED_STYLE = [Color.bold]
UNSELECTED_COLOR = Color.reset
UNSELECTED_STYLE = []

def get_change(key, cols):
    """Retrieves the change in option index based on the key pressed for navigation using 'WASD'.

    Args:
        key (bytes): The key pressed by the user.
        cols (int): Number of columns in the menu grid.

    Returns:
        int: The change in option index; negative for left/up movements, positive for right/down movements.
    """
    key_mappings = {
        b'a': -1,
        b'd': 1,
        b'w': -cols,
        b's': cols,
    }
    return key_mappings.get(key, 0)

def get_arrow_change(key, cols):
    """Retrieves the change in option index based on the arrow key pressed for navigation.

    Args:
        key (bytes): The key pressed by the user, specifically for arrow keys.
        cols (int): Number of columns in the menu grid.

    Returns:
        int: The change in option index; negative for left/up movements, positive for right/down movements.
    """
    arrow_mappings = {
        b'H': -cols,
        b'P': cols,
        b'K': -1,
        b'M': 1,
    }
    return arrow_mappings.get(key, 0)

def update_option(current_option, change, total_options):
    """Updates the current option index based on the change and wraps around if necessary.

    Args:
        current_option (int): The current selected option index.
        change (int): The change to be applied to the current option index.
        total_options (int): The total number of options available.

    Returns:
        int: The updated option index, wrapped around if it exceeds the total options.
    """
    return (current_option + change) % total_options

def display_menu(options, rows, cols, x=2, y=20, box_width=BOX_WIDTH):
    """Displays the menu in a grid of rows and columns, allowing navigation using the 'WASD' keys.

    Args:
        options (list): List of tuples containing the option text and corresponding action function.
        rows (int): Number of rows in the menu grid.
        cols (int): Number of columns in the menu grid.
        x (int, optional): The horizontal position (column) to display the menu.
        y (int, optional): The vertical position (line) to display the menu.
        box_width (int, optional): The width of each menu option box.
    """
    current_option = 0
    total_options = len(options)

    try:
        hide_cursor()
        while True:
            for row in range(rows):
                for col in range(cols):
                    index = row * cols + col
                    if index < total_options:
                        is_selected = index == current_option
                        color = SELECTED_COLOR if is_selected else UNSELECTED_COLOR
                        style = SELECTED_STYLE if is_selected else UNSELECTED_STYLE

                        move_cursor(x + col * (box_width + 2) + col, y + row * 3)
                        print_color(f"┌{'─' * box_width}┐", color, style)

                        option_text = options[index][0]
                        move_cursor(x + col * (box_width + 2) + col, y + row * 3 + 1)
                        print_color(f"│ {option_text:^{box_width - 2}} │", color, style)

                        move_cursor(x + col * (box_width + 2) + col, y + row * 3 + 2)
                        print_color(f"└{'─' * box_width}┘", color, style)

            key = msvcrt.getch()
            if key == b'\xe0':
                key = msvcrt.getch()
                change = get_arrow_change(key, cols)
            elif key == b' ':
                action = options[current_option][1]
                action()
                break
            else:
                change = get_change(key, cols)

            current_option = update_option(current_option, change, total_options)

    finally:
        show_cursor()
