import os
import msvcrt
from utils.colors import Color, print_color

BOX_WIDTH = 29
SELECTED_COLOR = Color.yellow
SELECTED_STYLE = [Color.bold]
UNSELECTED_COLOR = Color.white
UNSELECTED_STYLE = []

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def hide_cursor():
    """Hides the cursor."""
    print("\033[?25l", end='', flush=True)

def show_cursor():
    """Shows the cursor."""
    print("\033[?25h", end='', flush=True)

def display_menu(options, rows, cols):
    """Displays the menu in a grid of rows and columns, allowing navigation using the 'WASD' keys.

    Args:
        options (list): List of tuples containing the option text and corresponding action function.
        rows (int): Number of rows in the menu grid.
        cols (int): Number of columns in the menu grid.
    """
    current_option = 0
    total_options = len(options)

    hide_cursor()

    try:
        while True:
            clear_screen()

            for row in range(rows):
                for col in range(cols):
                    index = row * cols + col
                    if index < total_options:
                        color = SELECTED_COLOR if index == current_option else UNSELECTED_COLOR
                        style = SELECTED_STYLE if index == current_option else UNSELECTED_STYLE
                        print_color(f"┌{'─' * BOX_WIDTH}┐", color, style, end=' ')
                print()

                for col in range(cols):
                    index = row * cols + col
                    if index < total_options:
                        option, _ = options[index]
                        if index < total_options:
                            color = SELECTED_COLOR if index == current_option else UNSELECTED_COLOR
                            style = SELECTED_STYLE if index == current_option else UNSELECTED_STYLE
                            print_color(f"│ {option:^{BOX_WIDTH-2}} │", color, style, end=' ')
                print()

                for col in range(cols):
                    index = row * cols + col
                    if index < total_options:
                        if index < total_options:
                            color = SELECTED_COLOR if index == current_option else UNSELECTED_COLOR
                            style = SELECTED_STYLE if index == current_option else UNSELECTED_STYLE
                            print_color(f"└{'─' * BOX_WIDTH}┘", color, style, end=' ')
                print()

            key = msvcrt.getch()

            if key == b'a':
                current_option = (current_option - 1) % total_options
            elif key == b'w':
                current_option = (current_option - cols) % total_options
            elif key == b's':
                current_option = (current_option + cols) % total_options
            elif key == b'd':
                current_option = (current_option + 1) % total_options
            elif key == b' ':
                action = options[current_option][1]
                action()

    finally:
        show_cursor()
