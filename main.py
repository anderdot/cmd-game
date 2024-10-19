from data import globals
from utils.menu import display_menu
from utils.screen import clear_screen, set_cmd_window_size
from utils.cursor import move_cursor
from locales.loader import list_languages, load_language, load_default_language, count_languages
from graphics.loader import print_art
import msvcrt

def start_game():
    print("Starting game...")
    msvcrt.getch()

def open_settings():
    clear_screen()
    move_cursor(2, 1)

    settings = globals.language_data.get('settings', {})
    languages = list_languages()
    options = []

    for lang_code, lang_info in languages.items():
        option_text = lang_info['name']
        file_path = lang_info['file']
        options.append((option_text, lambda path=file_path: load_language(path)))

    display_menu(options, rows=count_languages(), cols=1, x=4, y=4, fullbox=True, text=settings.get('select_language'))

def about_game():
    print("About this game...")
    msvcrt.getch()

def exit_game():
    globals.settings.update({"loop": False})
    print("Exiting game...")
    msvcrt.getch()

def menu():
    clear_screen()
    set_cmd_window_size(150, 40)
    print_art('logo')

    start_menu = globals.language_data.get('start_menu', {})
    options_mapping = [
        (start_menu.get('start'), start_game),
        (start_menu.get('options'), open_settings),
        (start_menu.get('about'), about_game),
        (start_menu.get('exit'), exit_game)
    ]

    display_menu(options_mapping, rows=4, cols=1, x=59, y=27, box_width=30)

def main():
    load_default_language()
    while globals.settings.get('loop'):
        menu()

if __name__ == "__main__":
    main()
