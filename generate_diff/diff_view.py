SYMBOLS = {
    'added': '+',
    'removed': '-'
}


def render_diff(source, sep=''):
    result_view = {}
    for key, value in source.items():
        if isinstance(value, dict):
            if is_modified(value):
                for mod in value.keys():
                    mod_key = SYMBOLS[mod] + sep + key
                    if isinstance(value[mod], dict):
                        result_view[mod_key] = render_diff(value[mod], sep)
                    else:
                        result_view[mod_key] = value[mod]
            else:
                result_view[sep + key] = render_diff(value, sep)
        else:
            result_view[sep + key] = value
    return result_view


def print_(rendered_diff, indent=''):
    for key, value in rendered_diff.items():
        if isinstance(value, dict):
            print(f'{indent}{key}:')
            print_(value, indent + '    ')
        else:
            print(f'{indent}{key}: {value}')


def is_modified(value):
    return value.get('added') is not None or value.get('removed') is not None
