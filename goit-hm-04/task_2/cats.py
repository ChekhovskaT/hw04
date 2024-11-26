from pathlib import Path
from pprint import pprint

path = Path(__file__).parent

def get_cats_info(path):

    cats_info = []
    try:
        with open (path / "cats_info.txt", 'r', encoding='utf-8') as file:
            # Remove extra characters and split the string into parts
            for line in file:
                line = line.strip()
                parts = line.split(',')

                # Make sure the string contains three elements
                if len(parts) == 3:
                    cat_id, name, age = parts
                    # Create a dictionary and add it to the list
                    cats = { "id": cat_id, "name": name, "age": age}
                    cats_info.append(cats)
                else:
                    print(f'Invalid line format: {line}')

    except FileNotFoundError:
        print(f'File not found at {path}')
    except UnicodeDecodeError:
        print(f'Encoding error while reading file {path}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    
    return cats_info

# Example of using the function
cats_information = get_cats_info(path)
pprint(cats_information, sort_dicts=False)


