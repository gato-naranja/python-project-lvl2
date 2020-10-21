from generate_diff.generate_diff import load_from
from generate_diff.src.comparison import make_comparsion
from tests.fixtures.example_tests_data import simple_diff_data
from tests.fixtures.example_tests_data import simple_data_part_1
from tests.fixtures.example_tests_data import simple_data_part_2
from tests.fixtures.example_tests_data import simple_dict1, simple_dict2
from tests.fixtures.example_tests_data import complex_data_part1
from tests.fixtures.example_tests_data import complex_data_part2
from tests.fixtures.example_tests_data import complex_diff_data
from generate_diff.generate_diff import make_flat_view as mv


def test_diff_simple_files():
    fsd = simple_data_part_1()
    ssd = simple_data_part_2()
    assert mv(make_comparsion(fsd, ssd)) == simple_diff_data()


def test_load_simple_json_file():
    file_for_test = 'tests/fixtures/file1.json'
    assert load_from(file_for_test, '.json') == simple_dict1()


def test_load_simple_yaml_file():
    file_for_test = 'tests/fixtures/other_file2.yaml'
    assert load_from(file_for_test, '.yaml') == simple_dict2()


def test_load_complex_json_file():
    file_for_test = 'tests/fixtures/file3.json'
    return load_from(file_for_test, '.json') == complex_data_part1()


def test_load_complex_yaml_file():
    file_for_test = 'tests/fixtures/other_file4.yaml'
    return load_from(file_for_test, '.yaml') == complex_data_part2()


def test_diff_complex_files():
    fcd = complex_data_part1()
    scd = complex_data_part2()
    data = make_comparsion(fcd, scd)
    assert mv(data) == complex_diff_data()
