import json
import yaml
from os.path import abspath, splitext


def gendiff(first_data, second_data):
    result_diff = {}
    for key, value in second_data.items():
        if key in first_data:
            if second_data[key] == first_data[key]:
                result_diff[key] = first_data[key]
                first_data.pop(key)
            elif second_data[key] != first_data[key]:
                result_diff['- ' + key] = first_data[key]
                result_diff['+ ' + key] = second_data[key]
                first_data.pop(key)
        else:
            result_diff['+ ' + key] = second_data[key]
    result_diff.update(first_data)
    return result_diff


def load_from_file(user_file, file_format):
    with open(user_file, 'r') as file_load:
        if file_format == '.json':
            return json.load(file_load)
        elif file_format == '.yaml' or file_format == '.yml':
            return yaml.load(file_load, yaml.SafeLoader)


def get_diff(path_to_file1, path_to_file2):
    full_path1 = abspath(path_to_file1)
    full_path2 = abspath(path_to_file2)
    first_data = load_from_file(
        full_path1,
        splitext(full_path1)[1],
    )
    second_data = load_from_file(
        full_path2,
        splitext(full_path2)[1],
    )
    result = gendiff(
        first_data,
        second_data,
        )
    print('{')
    for key, value in result.items():
        print(f'    {key}: {value}')
    print('}')
