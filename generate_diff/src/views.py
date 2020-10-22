def get_diff_mod(value, empty=''):
    if isinstance(value, dict):
        mod = value.get('diff', 'next')
    else:
        mod = empty
    return mod


def make_flat_view(tree):
    result_view = {}
    for key, value in tree.items():
        diff_mod = get_diff_mod(value, empty='next')
        if diff_mod == 'added':
            actual_key = f'+{key}'
            result_view[actual_key] = value['major']
        elif diff_mod == 'removed':
            actual_key = f'-{key}'
            result_view[actual_key] = value['minor']
        elif diff_mod == 'updated':
            result_view[f'-{key}'] = value['from']
            result_view[f'+{key}'] = value['to']
        elif diff_mod == 'next' and isinstance(value, dict):
            result_view[key] = make_flat_view(value)
        else:
            result_view[key] = value
    return result_view


def is_complex(value, quotes=''):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f'{quotes}{value}{quotes}'


def make_message(mod, key, value, path):
    current_path = path + key
    message = f'Property \'{current_path}\' was {mod}'
    if mod == 'added':
        added_value = is_complex(value['major'])
        message += f' with value: {added_value}'
    elif mod == 'updated':
        removed_value = is_complex(value['from'], quotes='\'')
        added_value = is_complex(value['to'], quotes='\'')
        message += f' from {removed_value} to {added_value}'
    return message


def make_plain_view(tree):
    result_view = []

    def inner(subtree, path=''):
        for key, value in subtree.items():
            diff_mod = get_diff_mod(value)
            if diff_mod == 'next':
                current_path = path + key + '.'
                inner(value, path=current_path)
            elif diff_mod in ('added', 'removed', 'updated'):
                diff_description = make_message(diff_mod, key, value, path)
                result_view.append(diff_description)

    inner(tree)
    return result_view
