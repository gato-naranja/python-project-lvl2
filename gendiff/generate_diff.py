from gendiff.io import load_
from gendiff import tree
from gendiff.view.selector import choice


def generate_diff(source_file, modified_file, format='stylish'):
    handler = choice(format)
    return handler.render(
        tree.compare(
            load_(source_file),
            load_(modified_file),
        )
    )
