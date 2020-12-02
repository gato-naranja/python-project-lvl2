from generate_diff.cli import load_
from generate_diff import tree


def get_diff(source_file, modified_file, format):
    if format == 'stylish':
        from generate_diff.view import stylish as handler
    elif format == 'plain':
        from generate_diff.view import plain as handler
    elif format == 'json':
        from generate_diff.view import json as handler
    return handler.render(
        tree.compare(
            load_(source_file),
            load_(modified_file),
        )
    )
