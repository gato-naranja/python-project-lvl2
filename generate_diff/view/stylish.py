SYMBOLS = {
    'added': '+',
    'removed': '-'
}


def render_(source, sep=' '):
    result_view = {}
    for key, value in source.items():
        if is_modified(value):
            for mod in value.keys():
                mod_key = SYMBOLS[mod] + sep + key
                result_view[mod_key] = get_(value[mod], sep)
        else:
            indent = convert(sep)
            result_view[indent + key] = get_(value, sep)
    return result_view


def print_(rendered_diff, indent=''):
    for key, value in rendered_diff.items():
        if isinstance(value, dict):
            print(f'{indent}{key}:')
            print_(value, indent + '    ')
        else:
            print(f'{indent}{key}: {value}')


def is_modified(value):
    if isinstance(value, dict):
        added_mod = value.get('added')
        removed_mod = value.get('removed')
        return added_mod is not None or removed_mod is not None


def get_(value, sep):
    if isinstance(value, dict):
        return render_(value, sep)
    else:
        return value


def convert(symbol):
    if symbol == '':
        return ''
    else:
        return symbol + ' '
