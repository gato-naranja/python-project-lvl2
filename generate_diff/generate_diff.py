import json
import yaml
from os.path import abspath, splitext
from generate_diff.src.comparison import make_comparsion
from generate_diff.src.views import make_flat_view, make_plain_view


def load_from(user_file, file_format):
    with open(user_file, 'r') as file_load:
        if file_format == '.json':
            loaded_data = json.load(file_load)
        elif file_format == '.yaml' or file_format == '.yml':
            loaded_data = yaml.load(file_load, yaml.SafeLoader)
    return loaded_data


def get_diff(path_to_file1, path_to_file2, format):
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
    output_diff(result, format)


def output_diff(comparison_result, format):
    if format == '':
        output_view = make_flat_view(comparison_result)
        print(output_view)
    elif format == 'plain':
        output_view = make_plain_view(comparison_result)
        for elem in output_view:
            print(elem)
