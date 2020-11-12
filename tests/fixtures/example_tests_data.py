def simple_diff_data():
    return {
        'timeout': {
            'removed': 50,
            'added': 20
            },
        'verbose': {
            'added': True
            },
        'host': 'hexlet.io',
        'follow': {
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
                'added': False
            },
            'setting1': 'Value 1',
            'setting2': {
                'removed': 200
            },
            'setting3': {
                'removed': True,
                'added': {
                    'key': 'value'
                }
            },
            'setting4': {
                'added': 'blah blah',
            },
            'setting5': {
                'added': {
                    'key5': 'value5'
                }
            },
            'setting6': {
                'doge': {
                    'wow': {
                        'removed': 'too much',
                        'added': 'so much'
                        }
                    },
                'key': 'value',
                'ops': {
                    'added': 'vops',
                    }
                }
        },
        'group1': {
            'baz': {
                'removed': 'bas',
                'added': 'bars'
            },
            'foo': 'bar',
            'nest': {
                'removed': {
                    'key': 'value'
                    },
                'added': 'str'
            }
        },
        'group2': {
            'removed': {
                'abc': 12345,
                'deep': {
                    'id': 45,
                    }
                }
            },
        'group3': {
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
    return {
        '+ group3': {
            ' fee': 100500,
            ' deep': {
                ' id': {
                    ' number': 45
                    }
                }
            },
        ' common': {
            '+ setting5': {
                ' key5': 'value5'
                },
            ' setting1': 'Value 1',
            ' setting6': {
                ' key': 'value',
                ' doge': {
                    '- wow': 'too much',
                    '+ wow': 'so much'
                    },
                '+ ops': 'vops'
                },
            '+ setting4': 'blah blah',
            '- setting2': 200,
            '+ follow': False,
            '- setting3': True,
            '+ setting3': {
                ' key': 'value'
                }
            },
        '- group2': {
            ' abc': 12345,
            ' deep': {
                ' id': 45
                }
            },
        ' group1': {
            '- nest': {
                ' key': 'value'
                },
            '+ nest': 'str',
            '- baz': 'bas',
            '+ baz': 'bars',
            ' foo': 'bar'
            }
        }
