from enum import Enum

class Color(Enum):
    reset     = '\033[m'
    white     = '\033[30m'
    red       = '\033[31m'
    green     = '\033[32m'
    yellow    = '\033[33m'
    blue      = '\033[34m'
    purple    = '\033[35m'
    cyan      = '\033[36m'
    gray      = '\033[37m'

    bold      = '\033[1m'
    underline = '\033[4m'

    def __str__(self):
        return self.value

def print_color(text, color=Color.white, styles=None, end='\n'):
    """Print text with specific color and styles.

    Args:
        text (str): Text to print.
        color (Color, optional): Color to use. Defaults to Color.white.
        styles (list[Color], optional): List of styles to apply. Defaults to None.
    """
    if styles is None:
        styles = []

    styled_text = f"{''.join([str(style) for style in styles])}{text}"
    print(f"{color}{styled_text}{color.reset}", end=end)

def string_color(text, color=Color.white, styles=None):
    """Return a string with specific color and styles.

    Args:
        text (str): Text to print.
        color (Color, optional): Color to use. Defaults to Color.white.
        styles (list[Color], optional): List of styles to apply. Defaults to None.
    """
    if styles is None:
        styles = []

    styled_text = f"{''.join([str(style) for style in styles])}{text}"
    return f"{color}{styled_text}{color.reset}"
