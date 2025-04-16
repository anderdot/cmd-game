from data import globals
from utils.screen import set_window_default
from utils.cursor import hide_cursor, show_cursor
from locales.loader import load_default_language
from scenes.scene_manager import push_scene

def main():
    set_window_default()
    hide_cursor()
    load_default_language()
    push_scene('main_scene')
    # while globals.settings.get('loop'):
    show_cursor()

if __name__ == "__main__":
    main()
