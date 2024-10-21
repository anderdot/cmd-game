from data import globals
from utils.screen import clear_screen, set_window_default
from utils.cursor import move_cursor, hide_cursor, show_cursor
from locales.loader import list_languages, load_language, load_default_language, count_languages
from scenes.scene import main_scene
from inputs.input_handler import getkey

def start_game():
    options_mapping = [
        ("1", lambda: print("1...")),
        ("2", lambda: print("2...")),
        ("3", lambda: print("3...")),
        ("4", lambda: print("4...")),
        ("5", lambda: print("5...")),
        ("6", lambda: print("6...")),
        ("7", lambda: print("7...")),
        ("8", lambda: print("8...")),
    ]

    rows = 2  # Número de linhas visíveis de opções por página
    cols = 2  # Número de colunas visíveis de opções por página
    x = 1     # Posição horizontal de início
    y = 1     # Posição vertical de início
    box_width = 11  # Largura das caixas de opções

    # Criando e exibindo o menu com a barra de rolagem
    # menu = ScrollMenu(options_mapping, rows, cols, x, y, box_width)
    # menu.display()

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

    # display_menu(options, rows=count_languages(), cols=1, x=4, y=4, fullbox=True, text=settings.get('select_language'))
    move_cursor(2, globals.window_size.get('height') - 1)
    print(settings.get('selected_language'))

def about_game():
    pass

def exit_game():
    globals.settings.update({"loop": False})

def main():
    set_window_default()
    hide_cursor()
    load_default_language()
    while globals.settings.get('loop'):
        main_scene()
    show_cursor()
    getkey()

if __name__ == "__main__":
    main()
