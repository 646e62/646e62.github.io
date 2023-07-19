import os
import json

def format_definition(english_def, french_def, french_key):
    return f'("{english_def}", "{french_def}", "{french_key}")'


def prompt_definition():
    key = input('Please enter the English word or phrase: ')

    english_def = input('Please enter the English definition (separate list items with ";"): ')
    english_def = english_def.replace('; ', '",\n\t"').replace(';', '",\n\t"')
    
    french_def = input('Please enter the French definition (separate list items with ";"): ')
    french_def = french_def.replace('; ', '",\n\t"').replace(';', '",\n\t"')
    
    french_key = input('Please enter the French equivalent of the English key: ')

    return key, format_definition(english_def, french_def, french_key)


def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf8') as f:
        f.write("definitions = ")
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


def main():
    definitions = {}

    while True:
        key, definition = prompt_definition()
        definitions[key] = definition

        more = input('Do you want to enter another definition? (y/n): ')
        if more.lower() != 'y':
            break

    filename = input('Please enter a dictionary name for the file: ')
    filename = f"{filename}.txt"
    save_to_file(filename, definitions)

    print(f"Definitions have been written to {os.path.abspath(filename)}")


if __name__ == '__main__':
    main()
