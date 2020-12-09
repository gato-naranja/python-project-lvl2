from generate_diff.view import stylish
from generate_diff.view import plain
from generate_diff.view import json


def choice(format):
    if format == 'stylish':
        return stylish
    elif format == 'plain':
        return plain
    elif format == 'json':
        return json
