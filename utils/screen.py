import os
import ctypes
from data import globals
from utils.cursor import move_cursor

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_area(x, y, width, height):
    """Clears a specified rectangular area.

    Args:
        x (int): The horizontal position (column) of the area to clear.
        y (int): The vertical position (line) of the area to clear.
        height (int): The height of the area to clear.
        width (int): The width of the area to clear.
    """
    for i in range(height):
        move_cursor(x, y + i)
        print(" " * width, end='')

def set_cmd_window_size(cols, lines):
    """Sets the size of the command prompt (CMD) window in Windows.

    Args:
        cols (int): The number of columns (width) for the CMD window.
        lines (int): The number of lines (height) for the CMD window.
    """
    os.system(f'mode con: cols={cols} lines={lines}')

def disable_maximize_and_resize():
    """Disables the maximize button and prevents resizing the CMD window."""
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
        style &= ~0x00010000
        style &= ~0x00040000
        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

def set_window_position():
    """Sets the position of the CMD window on the screen."""
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.SetWindowPos(hwnd, 0, -6, 0, 0, 0, 0x0001)

def set_cmd_title():
    """Sets the title of the CMD window."""
    ctypes.windll.kernel32.SetConsoleTitleW('CMD Game')

def set_window_default():
    """Sets the default properties for the CMD window."""
    set_cmd_window_size(globals.window_size.get('width'), globals.window_size.get('height'))
    set_window_position()
    disable_maximize_and_resize()
    set_cmd_title()
