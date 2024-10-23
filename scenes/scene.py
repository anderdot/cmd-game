from menus.menu import main_menu
from menus.render import display_title, display_title_box, draw_box
from graphics.loader import print_art
from utils.screen import clear_screen
from locales.translation import get_size_text

def render_logo():
    x = (150 - size) // 2 - 1
    y = 12
    """Renders the logo"""
    print_art('logo')
    size = get_size_text('main.tribute')
    display_title('main.tribute', x, y)

def render_controls_box():
    """Renders the controls box."""
    x = 118
    y = 16
    box_width = 24
    box_height = 30
    display_title_box('main.controls', x, y, box_width, box_height)
    print_art('controls')

def render_main_menu_box():
    """Renders the main menu."""
    x = 56
    y = 20
    box_width = 39
    box_height = 19
    draw_box(x, y, box_width, box_height)
    main_menu()

def main_scene():
    """Main scene setup and display."""
    clear_screen()
    render_logo()
    render_controls_box()
    render_main_menu_box()
