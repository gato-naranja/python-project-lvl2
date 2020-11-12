from generate_diff.comparison import make_comparison
from tests.fixtures.example_tests_data import simple_diff_data
from tests.fixtures.example_tests_data import simple_data_part_1
from tests.fixtures.example_tests_data import simple_data_part_2
from tests.fixtures.example_tests_data import complex_data_part1
from tests.fixtures.example_tests_data import complex_data_part2
from tests.fixtures.example_tests_data import complex_diff_data
from generate_diff.diff_plain_view import make_plain_view
from tests.fixtures.example_tests_data import plain_data
from generate_diff.diff_view import render_diff
from tests.fixtures.example_tests_data import diff_view_structure


def test_diff_simple_files():
    fsd = simple_data_part_1()
    ssd = simple_data_part_2()
    assert make_comparison(fsd, ssd) == simple_diff_data()


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
    out_data_structure = diff_view_structure()
    diff_result = complex_diff_data()
    assert render_diff(diff_result, ' ') == out_data_structure
