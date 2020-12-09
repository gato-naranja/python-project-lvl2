from generate_diff.cli import load_
from generate_diff import tree
from generate_diff.view.selector import choice


def get_diff(source_file, modified_file, format):
    handler = choice(format)
    return handler.render(
        tree.compare(
            load_(source_file),
            load_(modified_file),
        )
    )
