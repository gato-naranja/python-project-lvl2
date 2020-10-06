from generate_diff.generate_diff import gendiff, load_from_file


def test_diff():
    diff_data = {
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True,
        'host': 'hexlet.io',
        'proxy': '123.234.53.22',
        'follow': False,
        }
    first_data = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }
    second_data = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }
    assert gendiff(first_data, second_data) == diff_data


def test_load_json_file():
    test_dict1 = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
        }
    file_for_test = 'tests/fixtures/file1.json'
    assert load_from_file(file_for_test, '.json') == test_dict1


def test_load_yaml_file():
    test_dict2 = {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io',
    }
    file_for_test = 'tests/fixtures/other_file2.yaml'
    assert load_from_file(file_for_test, '.yaml') == test_dict2
