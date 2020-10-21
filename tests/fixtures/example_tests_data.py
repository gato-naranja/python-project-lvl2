def simple_diff_data():
    return {
        '-timeout': 50,
        '+timeout': 20,
        '+verbose': True,
        'host': 'hexlet.io',
        '-proxy': '123.234.53.22',
        '-follow': 'false',
        }


def simple_data_part_1():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": 'false',
        }


def simple_data_part_2():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
        }


def simple_dict1():
    return {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
        }


def simple_dict2():
    return {
        'timeout': 50,
        'verbose': True,
        'host': 'hexlet.io',
        'type': 'education',
        }


def complex_diff_data():
    return {
        'common': {
            '+follow': "false",
            'setting1': 'Value 1',
            '-setting2': 200,
            '-setting3': "true",
            '+setting3': {
                'key': 'value'
                },
            '+setting4': 'blah blah',
            '+setting5': {
                'key5': 'value5',
                },
            'setting6': {
                'doge': {
                    '-wow': 'too much',
                    '+wow': 'so much',
                    },
                'key': 'value',
                '+ops': 'vops',
                }
            },
        'group1': {
            '-baz': 'bas',
            '+baz': 'bars',
            'foo': 'bar',
            '-nest': {
                'key': 'value'
                },
            '+nest': 'str',
            },
        '-group2': {
            'abc': 12345,
            'deep': {
                'id': 45,
                }
            },
        '+group3': {
            'fee': 100500,
            'deep': {
                'id': {
                    'number': 45,
                    }
                }
            }
        }


def complex_data_part1():
    return {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": 'true',
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": "too much"
                    }
                }
            },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
                }
            },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
                }
            }
        }


def complex_data_part2():
    return {
        'common': {
            'follow': 'false',
            'setting1': 'Value 1',
            'setting3': {
                'key': 'value',
                },
            'setting4': 'blah blah',
            'setting5': {
                'key5': 'value5'
                },
            'setting6': {
                'key': 'value',
                'ops': 'vops',
                'doge': {
                    'wow': 'so much',
                    }
                }
            },
        'group1': {
            'foo': 'bar',
            'baz': 'bars',
            'nest': 'str',
            },
        'group3': {
            'fee': 100500,
            'deep': {
                'id': {
                    'number': 45
                    }
                }
            }
        }
