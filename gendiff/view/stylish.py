def render(diff):
    view_lines = ['{']

    def walk(sub_tree, indent):
        for key, value in sub_tree.items():
            if key[0] not in ('+', '-'):
                key = '  ' + key
            if isinstance(value, dict):
                view_lines.append(f'{indent}{key}: {{')
                walk(value, indent + '    ')
            else:
                view_lines.append(f'{indent}{key}: {transmit(value)}')
        view_lines.append(f'{indent[:-2]}}}')

    walk(transform(diff), '  ')
    return '\n'.join(view_lines)


def transform(inner_tree):
    result = {}
    for key, value in inner_tree.items():
        if isinstance(value, dict):
            added = value.get('added')
            removed = value.get('removed')
            if removed is not None:
                mod_key = '-' + ' ' + key
                result[mod_key] = removed
            if added is not None:
                mod_key = '+' + ' ' + key
                result[mod_key] = added
            if added is None and removed is None:
                result[key] = transform(value)
        else:
            result[key] = value
    return result


def transmit(value):
    if value is False:
        transmitted = 'false'
    elif value is True:
        transmitted = 'true'
    elif value is None:
        transmitted = 'null'
    else:
        transmitted = value
    return transmitted
