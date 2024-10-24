import msvcrt
from enum import Enum
class Key(Enum):
    UP     = b'H'
    DOWN   = b'P'
    LEFT   = b'K'
    RIGHT  = b'M'
    W      = b'w'
    S      = b's'
    A      = b'a'
    D      = b'd'
    ACTION = b' '
    BACK   = b'q'

def getkey():
    """Get the key pressed by the user."""
    msvcrt.getch()
    return msvcrt.getch()

def get_key_change(key, rows, cols):
    """Change the position of the cursor based on the key pressed.

    Args:
        key (str): The key pressed by the user.
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.

    Returns:
        int: The change in the cursor position based on the key pressed.
    """
    key_mappings = {
        Key.W: -cols if rows > 1 else 0,
        Key.S: cols if rows > 1 else 0,
        Key.A: -1 if cols > 1 else 0,
        Key.D: 1 if cols > 1 else 0,
    }

    if key == b'\xe0':
        extended_key = getkey()
        return get_extended_key_change(extended_key, rows, cols)

    return key_mappings.get(Key(key), 0)

def get_extended_key_change(extended_key, rows, cols):
    """Key mappings for arrow keys

    Args:
        extended_key (str): The extended key pressed by the user.
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.

    Returns:
        int: The change in the cursor position based on the key pressed.
    """
    extended_key_mappings = {
        Key.UP: -cols if rows > 1 else 0,
        Key.DOWN: cols if rows > 1 else 0,
        Key.LEFT: -1 if cols > 1 else 0,
        Key.RIGHT: 1 if cols > 1 else 0,
    }

    return extended_key_mappings.get(Key(extended_key), 0)
