from data import globals

def get_translated_text(key, default=None):
    """ Returns the translated text for a given key.

    Args:
        key (str): The key to look up in the translation dictionary.
        default (str, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        str: The translated text, or the default value if the key is not found.
        int: The size of the translated text.
    """
    keys = key.split('.')
    translation = globals.language_data

    for k in keys:
        translation = translation.get(k, default)
        if translation is default:
            break
    size = len(translation) if translation else 0
    return translation, size

def get_size_text(key):
    """Returns the size of the translated text for a given key.

    Args:
        key (str): The key to look up in the translation dictionary.

    Returns:
        int: The size of the translated text.
    """
    keys = key.split('.')
    translation = globals.language_data

    for k in keys:
        translation = translation.get(k, None)
        if translation is None:
            break

    size = len(translation)
    return size
