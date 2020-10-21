import json
import yaml
from os.path import abspath, splitext
from generate_diff.src.comparison import make_comparsion


def load_from(user_file, file_format):
    with open(user_file, 'r') as file_load:
        if file_format == '.json':
            loaded_data = json.load(file_load)
        elif file_format == '.yaml' or file_format == '.yml':
            loaded_data = yaml.load(file_load, yaml.SafeLoader)
    return loaded_data


def make_flat_view(tree):
    result_view = {}
    for key, value in tree.items():
        if isinstance(value, dict):
            diff_mod = value.get('diff', 'next')
        else:
            diff_mod = 'next'
        if diff_mod == 'add':
            actual_key = f'+{key}'
            result_view[actual_key] = value['major']
        elif diff_mod == 'remove':
            actual_key = f'-{key}'
            result_view[actual_key] = value['minor']
        elif diff_mod == 'change':
            result_view[f'-{key}'] = value['minor']
            result_view[f'+{key}'] = value['major']
        elif diff_mod == 'next' and isinstance(value, dict):
            result_view[key] = make_flat_view(value)
        else:
            result_view[key] = value
    return result_view


def get_diff(path_to_file1, path_to_file2):
    full_path_file1 = abspath(path_to_file1)
    extension_file1 = splitext(full_path_file1)[1]
    full_path_file2 = abspath(path_to_file2)
    extension_file2 = splitext(full_path_file2)[1]
    first_data = load_from(
        full_path_file1,
        extension_file1,
    )
    second_data = load_from(
        full_path_file2,
        extension_file2,
    )
    result = make_comparsion(
        first_data,
        second_data,
        )
    output_view = make_flat_view(result)
    print(output_view)
