import json
import yaml
from os.path import abspath, splitext
from generate_diff.view import stylish
from generate_diff.view import plain
from generate_diff.view import v_json


def load_(file_name):
    path_to_source = abspath(file_name)
    file_format = splitext(path_to_source)[1]
    return extract_data(path_to_source, file_format)


def output_(diff, format):
    if format == 'stylish':
        handler = stylish
    elif format == 'plain':
        handler = plain
    elif format == 'json':
        handler = v_json
    visualization = handler.render_(diff)
    handler.print_(visualization)


def extract_data(file_name, extention):
    with open(file_name, 'r') as file_load:
        if extention == '.json':
            loaded_data = json.load(file_load)
        elif extention == '.yaml' or extention == '.yml':
            loaded_data = yaml.load(file_load, yaml.SafeLoader)
    return loaded_data
