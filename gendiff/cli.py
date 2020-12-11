import json
import yaml
import argparse
from os.path import abspath, splitext


def take_apart_params():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='stylish',
        help='set format of output',
    )
    return parser.parse_args()


def load_(file_name):
    path_to_source = abspath(file_name)
    file_format = splitext(path_to_source)[1]
    with open(path_to_source, 'r') as file_source:
        loaded_data = file_source.read()
    return parse(loaded_data, file_format)


def parse(data, _format):
    if _format == '.json':
        parsed = json.loads(data)
    elif _format in ('.yaml', '.yml'):
        parsed = yaml.load(data)
    return parsed
