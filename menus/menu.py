from .navigation import display_menu, display_tooltip, close_menu, exit_game
from locales.translation import get_translated_text

def main_menu():
    """Loads the main menu options and their corresponding actions."""
    main_menu, _ = get_translated_text('main.menu')
    options_mapping = [
        (main_menu.get('start').get('text'), lambda: display_tooltip("Starting game..."), main_menu.get('start').get('tooltip')),
        (main_menu.get('load').get('text'), lambda: display_tooltip("Continuing game..."), main_menu.get('load').get('tooltip')),
        (main_menu.get('options').get('text'), options_menu, main_menu.get('options').get('tooltip')),
        (main_menu.get('about').get('text'), lambda: display_tooltip("About game..."), main_menu.get('about').get('tooltip')),
        (main_menu.get('exit').get('text'), lambda: exit_game(), main_menu.get('exit').get('tooltip'))
    ]
    display_menu(options_mapping, rows=5, cols=1, x=60, y=22, box_width=31)

def options_menu():
    options_mapping = [
        ("Graphics", graphics_menu, "Modify graphics settings"),
        ("Sound", sound_menu, "Modify sound settings"),
        ("Back", lambda: close_menu(), "Return to the previous menu")
    ]
    display_menu(options_mapping, rows=2, cols=1, x=1, y=1, box_width=21)

def graphics_menu():
    options_mapping = [
        ("Resolution", lambda: display_tooltip("Adjusting resolution..."), "Change screen resolution"),
        ("Brightness", lambda: display_tooltip("Adjusting brightness..."), "Change screen brightness"),
        ("Back", lambda: close_menu(), "Return to the options menu")
    ]
    display_menu(options_mapping, rows=1, cols=2, x=30, y=1, box_width=21)

def sound_menu():
    options_mapping = [
        ("Volume", lambda: display_tooltip("Adjusting volume..."), "Change the volume level"),
        ("Mute", lambda: display_tooltip("Toggling mute..."), "Turn sound on or off"),
        ("Back", lambda: close_menu(), "Return to the options menu")
    ]
    display_menu(options_mapping, rows=1, cols=2, x=30, y=4, box_width=21)
