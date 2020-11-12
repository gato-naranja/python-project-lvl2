import json
import yaml
from os.path import abspath, splitext
from generate_diff.comparison import make_comparison
from generate_diff.diff_view import render_diff, print_
from generate_diff.diff_plain_view import make_plain_view


def get_diff(source_file, modified_file, format=''):
    path_to_source_file = abspath(source_file)
    path_to_modified_file = abspath(modified_file)
    source_data = load_from_file(
        path_to_source_file,
        splitext(path_to_source_file)[1],
    )
    modified_data = load_from_file(
        path_to_modified_file,
        splitext(path_to_modified_file)[1],
    )
    diff_files = make_comparison(
        source_data,
        modified_data,
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
        print_(
            render_diff(input_data, ' ')
        )
    elif format == 'plain':
        output_view = make_plain_view(input_data)
        for message in output_view:
            print(message)
    elif format == 'json':
        print(
            json.dumps(
                render_diff(input_data),
                indent=4
                )
        )
