import json
import pytest
from os.path import splitext
from generate_diff.view import stylish
from generate_diff.view import plain
from generate_diff.view import json as view_json
from generate_diff import tree


@pytest.fixture(params=[
    (stylish, 'tests/fixtures/complex_stylish_view.txt'),
    (plain, 'tests/fixtures/plain.txt'),
    (view_json, 'tests/fixtures/complex_json_view.json'),
])
def params_test(request):
    return request.param


def test_simple_diff():
    with open('tests/fixtures/simple_file1.json', 'r') as source_file:
        source = json.load(source_file)
    with open('tests/fixtures/simple_file2.json', 'r') as modified_file:
        modified = json.load(modified_file)
    with open('tests/fixtures/simple_stylish_view.txt', 'r') as view_file:
        expected = view_file.read()
    got_result = stylish.render(
        tree.compare(
            source,
            modified
        )
    )
    assert got_result == expected


def test_complex_diffs(params_test):
    output_format, reference_source = params_test
    with open('tests/fixtures/complex_file1.json', 'r') as source_file:
        source = json.load(source_file)
    with open('tests/fixtures/complex_file2.json', 'r') as modified_file:
        modified = json.load(modified_file)
    with open(reference_source, 'r') as diff_file:
        if splitext(reference_source)[1] == '.txt':
            expected = diff_file.read()
        else:
            expected = json.dumps(json.load(diff_file), indent=4)
    got_result = output_format.render(
        tree.compare(
            source,
            modified
        )
    )
    assert got_result == expected
