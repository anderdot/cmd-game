from menus.menu import main_menu, name_menu
from menus.render import display_title, display_title_box, draw_box
from graphics.loader import print_art
from utils.screen import clear_screen
from locales.translation import get_size_text
from data import globals

def render_logo():
    """Renders the logo"""
    size = get_size_text('main.tribute')
    x = (150 - size) // 2 - 1
    y = 12
    print_art('logo')
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

def render_name_box():
    """Renders the name box."""
    x = 61
    y = 10
    box_width = 30
    box_height = 3
    draw_box(x, y, box_width, box_height)

def render_keyboard_box():
    """Renders the keyboard box."""
    x = 12
    y = 17
    box_width = 127
    box_height = 17
    display_title_box('name.keyboard_text', x, y, box_width, box_height)

def name_scene():
    """scene of setting the player's name"""
    clear_screen()
    render_name_box()
    render_keyboard_box()
    name_menu()

def race_scene():
    """scene of setting the player's race"""
    clear_screen()
    print(globals.player.get('name'))
