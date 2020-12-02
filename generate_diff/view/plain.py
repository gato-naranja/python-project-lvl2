def render(diff):
    out_data = []

    def search_modified_nodes(sub_tree, path=''):
        for key, value in sub_tree.items():
            key_path = path + key
            if isinstance(value, dict):
                removed = value.get('removed')
                added = value.get('added')
                if removed is not None or added is not None:
                    out_data.append(make_message(removed, added, key_path))
                else:
                    search_modified_nodes(value, path=key_path + '.')

    search_modified_nodes(diff)
    return '\n'.join(out_data)


def make_message(val_removed, val_added, path):
    diff = get_status(val_removed, val_added)
    message = f'Property \'{path}\' was {diff}'
    if diff == 'added':
        added_value = extract_content(val_added)
        message += f' with value: {added_value}'
    elif diff == 'updated':
        removed_value = extract_content(val_removed, quotes='\'')
        added_value = extract_content(val_added, quotes='\'')
        message += f' from {removed_value} to {added_value}'
    return message


def get_status(val_old, val_new):
    if val_new is not None and val_old is None:
        return 'added'
    elif val_old is not None and val_new is None:
        return 'removed'
    elif val_new is not None and val_old is not None:
        return 'updated'


def extract_content(value, quotes=''):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f'{quotes}{transmit(value)}{quotes}'


def transmit(item):
    if item is False:
        transmitted = 'false'
    elif item is True:
        transmitted = 'true'
    elif item is None:
        transmitted = 'null'
    else:
        transmitted = item
    return transmitted
