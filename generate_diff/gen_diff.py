from generate_diff.io import load_, output_
from generate_diff.comparison import compare


def get_diff(source_file, modified_file, format):
    source_data = load_(source_file)
    modified_data = load_(modified_file)
    diffs = compare(source_data, modified_data)
    output_(diffs, format)
