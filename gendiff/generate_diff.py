from gendiff.cli import load_
from gendiff import tree
from gendiff.view.selector import choice


def gendiff(source_file, modified_file, format):
    handler = choice(format)
    return handler.render(
        tree.compare(
            load_(source_file),
            load_(modified_file),
        )
    )
