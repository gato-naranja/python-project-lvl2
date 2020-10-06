from generate_diff.generate_diff import gendiff


def test_diff():
    diff_data = {
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True,
        'host': 'hexlet.io',
        'proxy': '123.234.53.22',
        'follow': False,
        }
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    assert gendiff(first_file, second_file) == diff_data
