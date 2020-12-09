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
    return extract_data(path_to_source, file_format)


def extract_data(file_name, extention):
    with open(file_name, 'r') as file_load:
        if extention == '.json':
            loaded_data = json.load(file_load)
        elif extention == '.yaml' or extention == '.yml':
            loaded_data = yaml.load(file_load, yaml.SafeLoader)
    return loaded_data
