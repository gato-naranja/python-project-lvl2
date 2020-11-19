import json
from generate_diff.view.stylish import render_ as build_


def render_(diff):
    res_view = build_(diff, sep='')
    return json.dumps(res_view, indent=4)


def print_(view):
    print(view)
