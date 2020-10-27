# Example and structure changed elements:
# NODE = {
#     'diff':
#           - it can contain one of the following elements
#           'add', 'remove' or 'update'
#     'mod':
#           - it can contain one of the following elements
#           ['added], ['removed] or ['added', 'removed']
#     'added':
#           - contains the added value if they are
#     'removed':
#           - contains the removed value if they are
# }


from generate_diff.src.diff_model import get_diff, get_mod, get_action


SYMBOLS = {
    'added': '+',
    'removed': '-'
}


def make_diff_view(source_data):
    result_view = []

    def inner(sub_data, level=0):
        for key, value in sub_data.items():
            modificators = get_mod(value)
            if modificators is None:
                if isinstance(value, dict):
                    sub_view = construct_view_elem(key)
                    result_view.append((level, ' ', sub_view))
                    inner(value, level + 1)
                else:
                    sub_view = construct_view_elem(key, value)
                    result_view.append((level, ' ', sub_view))
            else:
                for mod in modificators:
                    mod_value = value[mod]
                    if isinstance(mod_value, dict):
                        sub_view = construct_view_elem(key)
                        result_view.append((level, SYMBOLS[mod], sub_view))
                        inner(mod_value, level + 1)
                    else:
                        sub_view = construct_view_elem(key, mod_value)
                        result_view.append((level, SYMBOLS[mod], sub_view))

    inner(source_data)
    return result_view


def construct_view_elem(key, value=None):
    return f'{key}:' if value is None else f'{key}: {value}'


def make_plain_view(source_data):
    result_view = []

    def inner(sub_data, path=''):
        for key, value in sub_data.items():
            diff = get_diff(value)
            key_path = path + key
            if diff == 'next':
                inner(value, path=key_path + '.')
            elif diff != 'next' and diff is not None:
                diff_description = make_message(value, key_path)
                result_view.append(diff_description)

    inner(source_data)
    return result_view


def make_message(value, path):
    action = get_action(value['mod'])
    message = f'Property \'{path}\' was {action}'
    if action == 'added':
        added_value = extract_content(value['added'])
        message += f' with value: {added_value}'
    elif action == 'updated':
        removed_value = extract_content(value['removed'], quotes='\'')
        added_value = extract_content(value['added'], quotes='\'')
        message += f' from {removed_value} to {added_value}'
    return message


def extract_content(value, quotes=''):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f'{quotes}{value}{quotes}'
