from pathlib import Path
from data import globals
from utils.storage import read_json

def list_races():
    """Lists all available races in .json races.

    Returns:
        dict: A list of races
    """
    data = read_json(Path('characters/races/races.json'))
    return data['races']

def get_race(race):
    """Gets a race by its name.

    Args:
        race_name (str): The name of the race to retrieve.

    Returns:
        dict: The race data if found, otherwise None.
    """
    races = list_races()
    return races.get(race)

def count_races():
    """Counts the number of available races.

    Returns:
        int: The number of races
    """
    races = list_races()
    return len(races)
