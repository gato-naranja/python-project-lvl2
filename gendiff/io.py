import json
import yaml
from os.path import abspath, splitext


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
        parsed = yaml.safe_load(data)
    return parsed
