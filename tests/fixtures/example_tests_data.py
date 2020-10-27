def simple_diff_data():
    return {
        'timeout': {
            'diff': 'update',
            'mod': ['removed', 'added'],
            'removed': 50,
            'added': 20
            },
        'verbose': {
            'diff': 'add',
            'mod': ['added'],
            'added': True
            },
        'host': 'hexlet.io',
        'follow': {
            'diff': 'remove',
            'mod': ['removed'],
            'removed': False,
            }
        }


def simple_data_part_1():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "follow": False,
        }


def simple_data_part_2():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
        }


def complex_diff_data():
    return {
        'common': {
            'follow': {
                'diff': 'add',
                'mod': ['added'],
                'added': False
            },
            'setting1': 'Value 1',
            'setting2': {
                'diff': 'remove',
                'mod': ['removed'],
                'removed': 200
            },
            'setting3': {
                'diff': 'update',
                'mod': ['removed', 'added'],
                'removed': True,
                'added': {
                    'key': 'value'
                }
            },
            'setting4': {
                'diff': 'add',
                'mod': ['added'],
                'added': 'blah blah',
            },
            'setting5': {
                'diff': 'add',
                'mod': ['added'],
                'added': {
                    'key5': 'value5'
                }
            },
            'setting6': {
                'doge': {
                    'wow': {
                        'diff': 'update',
                        'mod': ['removed', 'added'],
                        'removed': 'too much',
                        'added': 'so much'
                        }
                    },
                'key': 'value',
                'ops': {
                    'diff': 'add',
                    'mod': ['added'],
                    'added': 'vops',
                    }
                }
        },
        'group1': {
            'baz': {
                'diff': 'update',
                'mod': ['removed', 'added'],
                'removed': 'bas',
                'added': 'bars'
            },
            'foo': 'bar',
            'nest': {
                'diff': 'update',
                'mod': ['removed', 'added'],
                'removed': {
                    'key': 'value'
                    },
                'added': 'str'
            }
        },
        'group2': {
            'diff': 'remove',
            'mod': ['removed'],
            'removed': {
                'abc': 12345,
                'deep': {
                    'id': 45,
                    }
                }
            },
        'group3': {
            'diff': 'add',
            'mod': ['added'],
            'added': {
                'fee': 100500,
                'deep': {
                    'id': {
                        'number': 45
                        }
                    }
                }
            }
        }


def complex_data_part1():
    return {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
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
            'follow': False,
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


def plain_data():
    t = [
        "Property 'common.follow' was added with value: False",
        "Property 'common.setting2' was removed",
        "Property 'common.setting3' was updated from 'True' to [complex value]",
        "Property 'common.setting4' was added with value: blah blah",
        "Property 'common.setting5' was added with value: [complex value]",
        "Property 'common.setting6.doge.wow' was updated from 'too much' to 'so much'",
        "Property 'common.setting6.ops' was added with value: vops",
        "Property 'group1.baz' was updated from 'bas' to 'bars'",
        "Property 'group1.nest' was updated from [complex value] to 'str'",
        "Property 'group2' was removed",
        "Property 'group3' was added with value: [complex value]",
            ]
    return t


def diff_view_structure():
    return [
        (0, '-', 'group2:'),
        (1, ' ', 'abc: 12345'),
        (1, ' ', 'deep:'),
        (2, ' ', 'id: 45'),
        (0, '+', 'group3:'),
        (1, ' ', 'fee: 100500'),
        (1, ' ', 'deep:'),
        (2, ' ', 'id:'),
        (3, ' ', 'number: 45'),
        (0, ' ', 'common:'),
        (1, ' ', 'setting6:'),
        (2, ' ', 'doge:'),
        (3, '-', 'wow: too much'),
        (3, '+', 'wow: so much'),
        (2, '+', 'ops: vops'),
        (2, ' ', 'key: value'),
        (1, '-', 'setting3: True'),
        (1, '+', 'setting3:'),
        (2, ' ', 'key: value'),
        (1, '+', 'follow: False'),
        (1, ' ', 'setting1: Value 1'),
        (1, '+', 'setting4: blah blah'),
        (1, '-', 'setting2: 200'),
        (1, '+', 'setting5:'),
        (2, ' ', 'key5: value5'),
        (0, ' ', 'group1:'),
        (1, '-', 'nest:'),
        (2, ' ', 'key: value'),
        (1, '+', 'nest: str'),
        (1, '-', 'baz: bas'),
        (1, '+', 'baz: bars'),
        (1, ' ', 'foo: bar')
        ]
