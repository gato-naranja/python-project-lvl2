import json
import yaml
from os.path import abspath, splitext
from generate_diff.src.comparison import make_comparison
from generate_diff.src.views import make_diff_view, make_plain_view


def get_diff(file1, file2, format=''):
    path_to_file1 = abspath(file1)
    path_ti_file2 = abspath(file2)
    first_data = load_from_file(
        path_to_file1,
        splitext(path_to_file1)[1],
    )
    second_data = load_from_file(
        path_ti_file2,
        splitext(path_ti_file2)[1],
    )
    diff_files = make_comparison(
        first_data,
        second_data,
    )
    output_diffs(diff_files, format)


def load_from_file(user_file, file_format):
    with open(user_file, 'r') as file_load:
        if file_format == '.json':
            loaded_data = json.load(file_load)
        elif file_format == '.yaml' or file_format == '.yml':
            loaded_data = yaml.load(file_load, yaml.SafeLoader)
    return loaded_data


def output_diffs(input_data, format):
    if format == '':
        output_view = make_diff_view(input_data)
    elif format == 'plain':
        output_view = make_plain_view(input_data)
    print_view(output_view)


def print_view(maked_view):
    for elem in maked_view:
        output = make_string(elem)
        print(output)


def make_string(view_elem):
    if isinstance(view_elem, tuple):
        INDENT = '    '
        result = f'{INDENT * view_elem[0]}{view_elem[1]} {view_elem[2]}'
    else:
        result = view_elem
    return result
