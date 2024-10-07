import os
import ctypes

def hide_cursor():
    """Hides the cursor in the terminal."""
    if os.name == 'nt':
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        class CONSOLE_CURSOR_INFO(ctypes.Structure):
            _fields_ = [("dwSize", ctypes.c_int), ("bVisible", ctypes.c_bool)]

        cursor_info = CONSOLE_CURSOR_INFO()
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(cursor_info))
        cursor_info.bVisible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(cursor_info))

def show_cursor():
    """Shows the cursor in the terminal."""
    if os.name == 'nt':
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        class CONSOLE_CURSOR_INFO(ctypes.Structure):
            _fields_ = [("dwSize", ctypes.c_int), ("bVisible", ctypes.c_bool)]

        cursor_info = CONSOLE_CURSOR_INFO()
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(cursor_info))
        cursor_info.bVisible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(cursor_info))

def move_cursor(x = 0, y = 0):
    """Move the cursor to a specific position in the terminal.

    Args:
        x (int, optional): The horizontal position (column) to move the cursor to.
        y (int, optional): The vertical position (line) to move the cursor to.
    """
    print(f"\033[{y};{x}H", end='', flush=True)
