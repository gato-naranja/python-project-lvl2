from gendiff.view import stylish
from gendiff.view import plain
from gendiff.view import json


def choice(format):
    if format == 'stylish':
        return stylish
    elif format == 'plain':
        return plain
    elif format == 'json':
        return json
