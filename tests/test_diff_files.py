from generate_diff.gen_diff import load_from_file
from generate_diff.src.comparison import make_comparison
from tests.fixtures.example_tests_data import simple_diff_data
from tests.fixtures.example_tests_data import simple_data_part_1
from tests.fixtures.example_tests_data import simple_data_part_2
from tests.fixtures.example_tests_data import complex_data_part1
from tests.fixtures.example_tests_data import complex_data_part2
from tests.fixtures.example_tests_data import complex_diff_data
from generate_diff.src.views import make_plain_view
from tests.fixtures.example_tests_data import plain_data
from generate_diff.src.views import make_diff_view
from tests.fixtures.example_tests_data import diff_view_structure
from generate_diff.src.views import make_json_view
from tests.fixtures.example_tests_data import simple_json_data
from tests.fixtures.example_tests_data import complex_json_data


def test_diff_simple_files():
    fsd = simple_data_part_1()
    ssd = simple_data_part_2()
    assert make_comparison(fsd, ssd) == simple_diff_data()


def test_load_simple_json_file():
    file_for_test = 'tests/fixtures/file1.json'
    assert load_from_file(file_for_test, '.json') == simple_data_part_1()


def test_load_simple_yaml_file():
    file_for_test = 'tests/fixtures/other_file2.yaml'
    assert load_from_file(file_for_test, '.yaml') == simple_data_part_2()


def test_load_complex_json_file():
    file_for_test = 'tests/fixtures/file3.json'
    assert load_from_file(file_for_test, '.json') == complex_data_part1()


def test_load_complex_yaml_file():
    file_for_test = 'tests/fixtures/other_file4.yaml'
    assert load_from_file(file_for_test, '.yaml') == complex_data_part2()


def test_diff_complex_files():
    fcd = complex_data_part1()
    scd = complex_data_part2()
    data = make_comparison(fcd, scd)
    assert data == complex_diff_data()


def test_plain_view():
    data = complex_diff_data()
    view = make_plain_view(data)
    assert view == plain_data()


def test_diff_view():
    out_data_structure = sorted(diff_view_structure())
    diff_result = complex_diff_data()
    assert sorted(make_diff_view(diff_result)) == out_data_structure


def test_simple_json_view():
    diff_result = simple_diff_data()
    view = make_json_view(diff_result)
    assert view[0] == simple_json_data()


def test_complex_json_view():
    diff_result = complex_diff_data()
    view = make_json_view(diff_result)
    assert view[0] == complex_json_data()
