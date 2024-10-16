from pathlib import Path
from data import globals
from utils.storage import read_json

def list_languages():
    """Lists all available languages in .json languages.

    Returns:
        dict: A list of languages with status and location in directory.
    """
    data = read_json(Path('locales/languages.json'))
    return data['languages']

def load_language(language_path):
    """Loads the content of a specific language file from the locales directory.

    Args:
        lang_code (str): The language code corresponding to the .json file to load.
    """
    global language_data
    data = read_json(Path(language_path))
    globals.language_data = data

def load_default_language():
    """Loads the content of the default language file from the locales directory.

    Returns:
        dict: The loaded default language data from the JSON file.
    """
    default = read_json(Path('locales/languages.json'))['default_language']
    languages = list_languages()
    load_language(languages[default]['file'])

def count_languages():
    """Counts the number of available languages in the locales directory.

    Returns:
        int: The number of languages found in the directory.
    """
    languages = list_languages()
    return len(languages)
