from menus.menu import main_menu
from menus.render import display_title, draw_box
from graphics.loader import print_art
from utils.screen import clear_screen
from data import globals

def render_controls_box(x, y):
    """Renders the controls box at the given coordinates (x, y)."""
    box_width = 24
    box_height = 30
    draw_box(x, y, box_width, box_height)
    main_menu = globals.language_data.get('main_menu', {})
    title = main_menu.get('controls')
    length = len(title)
    display_title(title, x + (box_width - length - 2) // 2, y - 1)
    print_art('controls')

def main_scene():
    """Main scene setup and display."""
    clear_screen()
    print_art('logo')
    render_controls_box(118, 16)
    main_menu()
