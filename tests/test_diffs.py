import json
from generate_diff.view import stylish
from generate_diff.view import plain
from generate_diff.view import v_json
from generate_diff.comparison import compare


def test_diff_simple():
    with open('tests/fixtures/simple_file1.json', 'r') as source_file:
        source = json.load(source_file)
    with open('tests/fixtures/simple_file2.json', 'r') as modified_file:
        modified = json.load(modified_file)
    with open('tests/fixtures/simple_diff.json', 'r') as diff_file:
        reference_data = json.load(diff_file)
    comparison_result = compare(source, modified)
    assert comparison_result == reference_data


def test_diff_complex():
    with open('tests/fixtures/complex_file1.json', 'r') as source_file:
        source = json.load(source_file)
    with open('tests/fixtures/complex_file2.json', 'r') as modified_file:
        modified = json.load(modified_file)
    with open('tests/fixtures/complex_diff.json', 'r') as diff_file:
        reference_data = json.load(diff_file)
    comparison_result = compare(source, modified)
    assert comparison_result == reference_data


def test_stylish_simple():
    with open('tests/fixtures/simple_diff.json', 'r') as source_file:
        loaded_data = json.load(source_file)
    with open('tests/fixtures/simple_stylish_view.json', 'r') as view_file:
        reference_data = json.load(view_file)
    diff_view = stylish.render_(loaded_data)
    assert diff_view == reference_data


def test_stylish_complex():
    with open('tests/fixtures/complex_diff.json', 'r') as source_file:
        loaded_data = json.load(source_file)
    with open('tests/fixtures/complex_stylish_view.json', 'r') as view_file:
        reference_data = json.load(view_file)
    diff_view = stylish.render_(loaded_data)
    assert diff_view == reference_data


def test_plain():
    with open('tests/fixtures/plain.txt', 'r', encoding='utf8') as plain_file:
        reference_data = []
        for line in plain_file.readlines():
            reference_data.append(line[:-1])
    with open('tests/fixtures/complex_diff.json', 'r') as source_file:
        loaded_data = json.load(source_file)
    diff_view = plain.render_(loaded_data)
    assert diff_view == reference_data


def test_json():
    with open('tests/fixtures/complex_diff.json', 'r') as source_file:
        loaded_data = json.load(source_file)
    with open('tests/fixtures/complex_json_view.json', 'r') as view_file:
        reference_data = json.load(view_file)
    diff_view = v_json.render_(loaded_data)
    assert diff_view == json.dumps(reference_data, indent=4)
