def render(diff):
    out_data = ['{']

    def walk(sub_tree, indent):
        for key, value in sub_tree.items():
            if isinstance(value, dict):
                out_data.append(f'{indent}{key}: {{')
                walk(value, indent + '    ')
            else:
                out_data.append(f'{indent}{key}: {transmit(value)}')
        out_data.append(f'{indent}}}')

    tree = transform(diff)
    walk(tree, '')
    return '\n'.join(out_data)


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
                result['  ' + key] = transform(value)
        else:
            result['  ' + key] = value
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
