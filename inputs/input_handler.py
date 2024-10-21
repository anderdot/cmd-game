import msvcrt
from enum import Enum

def getkey():
    return msvcrt.getch()

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

def get_key_change(key, rows, cols):
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
    extended_key_mappings = {
        Key.UP: -cols if rows > 1 else 0,
        Key.DOWN: cols if rows > 1 else 0,
        Key.LEFT: -1 if cols > 1 else 0,
        Key.RIGHT: 1 if cols > 1 else 0,
    }
    return extended_key_mappings.get(Key(extended_key), 0)
