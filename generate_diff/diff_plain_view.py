def make_plain_view(diff):
    result_view = []

    def search_modified_nodes(sub_data, path=''):
        for key, value in sub_data.items():
            key_path = path + key
            if isinstance(value, dict):
                if is_modified(value):
                    result_view.append(make_message(value, key_path))
                else:
                    search_modified_nodes(value, path=key_path + '.')

    search_modified_nodes(diff)
    return result_view


def is_modified(value):
    return value.get('added') is not None or value.get('removed') is not None


def make_message(value, path):
    diff_status = get_status(value)
    message = f'Property \'{path}\' was {diff_status}'
    if diff_status == 'added':
        added_value = extract_content(value['added'])
        message += f' with value: {added_value}'
    elif diff_status == 'updated':
        removed_value = extract_content(value['removed'], quotes='\'')
        added_value = extract_content(value['added'], quotes='\'')
        message += f' from {removed_value} to {added_value}'
    return message


def get_status(value):
    status_added = value.get('added')
    status_removed = value.get('removed')
    if status_added is not None and status_removed is None:
        return 'added'
    elif status_removed is not None and status_added is None:
        return 'removed'
    elif status_added is not None and status_removed is not None:
        return 'updated'


def extract_content(value, quotes=''):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f'{quotes}{value}{quotes}'
