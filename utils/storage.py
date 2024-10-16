import json

def read_json(file_path):
    """Reads a JSON file and returns the data contained in it.

    Args:
        file_path (str): The path to the JSON file to be read.

    Returns:
        dict: The data contained in the JSON file.

    Raises:
        FileNotFoundError: If the file is not found.
        json.JSONDecodeError: If there is an error decoding the JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in the file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def read_txt(file_path):
    """Reads a text file and returns its content.

    Args:
        file_path (str): The path to the text file to be read.

    Returns:
        str: The content of the text file.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
