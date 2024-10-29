from data import globals
from utils.screen import set_window_default
from utils.cursor import hide_cursor, show_cursor
from locales.loader import load_default_language
from scenes.scene import main_scene, name_scene

def start_game():
    pass

def open_settings():
    pass

def about_game():
    pass

def main():
    set_window_default()
    hide_cursor()
    load_default_language()
    while globals.settings.get('loop'):
        main_scene()
    show_cursor()

if __name__ == "__main__":
    main()
