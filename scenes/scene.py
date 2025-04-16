from menus.menu import main_menu, name_menu, race_menu
from menus.render import display_title, display_title_box, display_title_box_with_text, draw_box
from graphics.loader import print_art
from utils.screen import clear_screen
from locales.translation import get_size_text
from characters.races.loader import get_race

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

def render_race_art_box(race):
    """Renders the race box."""
    x = 8
    y = 9
    box_width = 68
    box_height = 30
    draw_box(x, y, box_width, box_height)
    print_art(race, box=True)

def render_race_features_box(race):
    """Renders the race features box."""
    x = 77
    y = 9
    box_width = 67
    box_height = 30
    draw_box(x, y, box_width, box_height)

def render_race_option(race):
    """Renders the art for the given race.
    Args:
        race (str): The race for which to render the art.
    """
    x = 20
    y = 3
    width = 18
    height = 5
    spacing = 19
    race_status = get_race(race)
    for i, (attribute, value) in enumerate(race_status.items()):
        display_title_box_with_text(f'attributes.{attribute}', value, x + i * spacing, y, width, height, 'center')

    render_race_art_box(race)
    render_race_features_box(race)

def render_race_selector_box():
    """Renders the selector race box."""
    x = 8
    y = 39
    box_width = 136
    box_height = 6
    draw_box(x, y, box_width, box_height)

def render_attribute_box():
    """Renders the race attribute box."""
    x = 8
    y = 1
    box_width = 136
    box_height = 8
    draw_box(x, y, box_width, box_height)

def race_scene():
    """scene of setting the player's race"""
    clear_screen()
    render_race_selector_box()
    render_attribute_box()
    render_race_option('human')
    race_menu()
