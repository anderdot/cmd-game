from enum import Enum

class Color(Enum):
    reset        = '\033[0m'
    black        = '\033[30m'
    red          = '\033[31m'
    green        = '\033[32m'
    yellow       = '\033[33m'
    blue         = '\033[34m'
    purple       = '\033[35m'
    cyan         = '\033[36m'
    gray         = '\033[37m'
    light_red    = '\033[91m'
    light_green  = '\033[92m'
    light_yellow = '\033[93m'
    light_blue   = '\033[94m'
    light_purple = '\033[95m'
    light_cyan   = '\033[96m'
    light_gray   = '\033[97m'

    bold         = '\033[1m'
    underline    = '\033[4m'
    reverse      = '\033[7m'

    def __str__(self):
        return self.value

def apply_styles(text, styles=[]):
    """Apply styles to text.

    Args:
        text (str): Text to apply styles to.
        styles (list[Color], optional): List of styles to apply.

    Returns:
        str: Text with applied styles.
    """
    styled_text = f"{''.join([str(style) for style in styles])}{text}"
    return styled_text

def apply_format(text, format=None):
    """Apply format to text.

    Args:
        text (str): Text to apply format to.
        format (str, optional): Format to apply.

    Returns:
        str: Text with applied format.
    """
    if format is None:
        formatted_text = text
    elif 'f' in format:
        try:
            formatted_text = f"{float(text):{format}}"
        except ValueError:
            formatted_text = text
    else:
        formatted_text = f"{text:{format}}"

    return formatted_text

def print_color(text, color=Color.reset, reset=Color.reset, styles=[], format=None, end='\n'):
    """Print text with specific color and styles.

    Args:
        text (str): Text to print.
        color (Color, optional): Color to use.
        reset (Color, optional): Color to reset.
        styles (list[Color], optional): List of styles to apply.
        format (str, optional): Format to apply.
        end (str, optional): String to print at the end.
    """
    styled_text = apply_styles(text, styles)
    formatted_text = apply_format(styled_text, format)
    print(f"{color}{formatted_text}{reset}", end=end)

def string_color(text, color=Color.reset, reset=Color.reset, styles=[], format=None):
    """Return a string with specific color and styles.

    Args:
        text (str): Text to print.
        color (Color, optional): Color to use.
        reset (Color, optional): Reset color.
        styles (list[Color], optional): List of styles to apply.
        format (str, optional): Format to apply.

    Returns:
        str: String with applied color, format and styles.
    """
    styled_text = apply_styles(text, styles)
    formatted_text = apply_format(styled_text, format)
    final_text = f"{color}{formatted_text}{reset}"
    return final_text
