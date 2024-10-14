import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def set_cmd_window_size(cols, lines):
    """Sets the size of the command prompt (CMD) window in Windows.

    Args:
        cols (int): The number of columns (width) for the CMD window.
        lines (int): The number of lines (height) for the CMD window.
    """
    os.system(f'mode con: cols={cols} lines={lines}')
