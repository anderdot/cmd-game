from .navigation import display_menu, display_tooltip, close_menu, exit_game
from locales.translation import get_translated_text
from utils.cursor import move_cursor
from data import globals

def main_menu():
    """Loads the main menu options and their corresponding actions."""
    from scenes.scene_manager import push_scene
    main_menu, _ = get_translated_text('main.menu')
    options_mapping = [
        (main_menu.get('start').get('text'), main_menu.get('start').get('tooltip'), lambda: push_scene('name_scene')),
        (main_menu.get('load').get('text'), main_menu.get('load').get('tooltip'), lambda: display_tooltip("Continuing game...")),
        (main_menu.get('options').get('text'), main_menu.get('options').get('tooltip'), options_menu),
        (main_menu.get('about').get('text'), main_menu.get('about').get('tooltip'), lambda: display_tooltip("About game...")),
        (main_menu.get('exit').get('text'), main_menu.get('exit').get('tooltip'), lambda: exit_game())
    ]
    display_menu(options_mapping, rows=5, cols=1, x=60, y=22, box_width=31)

def options_menu():
    options_mapping = [
        ("Graphics", "Modify graphics settings", graphics_menu)
        ("Sound", "Modify sound settings", sound_menu)
        ("Back", "Return to the previous menu", lambda: close_menu())
    ]
    display_menu(options_mapping, rows=2, cols=1, x=1, y=1, box_width=21)

def graphics_menu():
    options_mapping = [
        ("Resolution", "Change screen resolution", lambda: display_tooltip("Adjusting resolution...")),
        ("Brightness", "Change screen brightness", lambda: display_tooltip("Adjusting brightness...")),
        ("Back", "Return to the options menu", lambda: close_menu())
    ]
    display_menu(options_mapping, rows=1, cols=2, x=30, y=1, box_width=21)

def sound_menu():
    options_mapping = [
        ("Volume", "Change the volume level", lambda: display_tooltip("Adjusting volume...")),
        ("Mute", "Turn sound on or off", lambda: display_tooltip("Toggling mute...")),
        ("Back", "Return to the options menu", lambda: close_menu())
    ]
    display_menu(options_mapping, rows=1, cols=2, x=30, y=4, box_width=21)

def name_menu():
    """Displays character selection for creating a player's name."""
    MAX_NAME_LENGTH = 16
    upper_case = True
    selected_chars = []

    def toggle_case(case=None):
        """Toggle between uppercase and lowercase letters.

        Args:
            case (bool, optional): If provided, set case explicitly.
        """
        nonlocal upper_case
        old_case = upper_case
        upper_case = not upper_case if case is None else case
        if old_case != upper_case:
            display_menu_options()

    def add_char(char):
        """Add a character to the selected name.

        Args:
            char (str): Character to add, adjusted based on current case.
        """
        if len(selected_chars) < MAX_NAME_LENGTH:
            selected_chars.append(char.upper() if upper_case else char.lower())
            display_selected_chars()
            toggle_case(selected_chars[-1] == " ")

    def delete_char():
        """Delete the last character from the selected name."""
        if selected_chars:
            selected_chars.pop()
            display_selected_chars()
            toggle_case(not selected_chars or selected_chars[-1] == " ")

    def clear_display():
        """Clear the display area where selected name is shown."""
        move_cursor(62, 11)
        display_width = 28
        print(" " * display_width, end="")

    def display_selected_chars():
        """Display the current state of the selected name with a cursor."""
        clear_display()
        selected_name = "".join(selected_chars)
        x_center = (globals.window_size.get('width') - len(selected_name) + 2) // 2
        move_cursor(x_center, 11)
        print(f"{selected_name}", end="_")

    def save_name():
        """Confirm the selected name."""
        from scenes.scene_manager import push_scene
        if not selected_chars:
            return
        globals.player.update({"name": "".join(selected_chars)})
        push_scene('race_scene')

    def display_menu_options():
        """Display character selection options for the name entry."""
        available_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        options_mapping = []
        name_menu, _ = get_translated_text('name.menu')
        for i, char in enumerate(available_chars):
            options_mapping.append(
                (char.upper() if upper_case else char.lower(), "", lambda c=char: add_char(c))
            )
            if i == 8:
                options_mapping.append((name_menu.get('delete').get('text'), name_menu.get('delete').get('tooltip'), delete_char))
            elif i == 17:
                options_mapping.append((name_menu.get('space').get('text'), name_menu.get('space').get('tooltip'), lambda c=' ': add_char(c)))
            elif i == 26:
                options_mapping.append((name_menu.get('toggle').get('text'), name_menu.get('toggle').get('tooltip'), toggle_case))
            elif i == 35:
                options_mapping.append((name_menu.get('save').get('text'), name_menu.get('save').get('tooltip'), save_name))

        display_menu(options_mapping, rows=4, cols=10, x=16, y=20, box_width=11)
    display_selected_chars()
    display_menu_options()

def race_menu():
    """Displays the race selection menu for the player."""
    from characters.races.loader import list_races
    from scenes.scene import render_race_option
    from utils.filters import filter_common_keys

    races = list_races()
    translated_races, _ = get_translated_text('races.menu')
    races, translated_races = filter_common_keys(races, translated_races)
    options_mapping = [
        (
            translated_races.get(race).get('name'),
            translated_races.get(race).get('description'),
            lambda r=race: save_race(r),
            lambda r=race: render_race_option(r)
        )
        for race in translated_races.keys()
    ]
    display_menu(options_mapping, rows=1, cols=5, x=11, y=40, box_width=25)

    def save_race(race):
        """Confirm the selected race."""
        from scenes.scene_manager import push_scene
        globals.player.update({"race": race})
        push_scene('class_scene')


