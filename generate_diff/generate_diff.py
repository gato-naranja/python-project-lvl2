import json
from os.path import abspath


def gendiff(first_file, second_file):
    with open(first_file, 'r') as ff:
        first_data = json.load(ff)
    with open(second_file, 'r') as sf:
        second_data = json.load(sf)
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


def get_diff(path_1, path_2):
    result = gendiff(
        abspath(path_1),
        abspath(path_2),
        )
    print('{')
    for key, value in result.items():
        print(f'    {key}: {value}')
    print('}')
