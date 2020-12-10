def compare(source_data, modified_data):
    return dict(
        map(
            lambda x: (
                x,
                collect_diff_values(
                    source_data.get(x, '#no#'),
                    modified_data.get(x, '#no#')
                )
            ),
            sorted(set(source_data.keys()) | set(modified_data.keys()))
        )
    )


def collect_diff_values(source, modified):
    source = transmit(source)
    modified = transmit(modified)
    if source == modified:
        result = modified
    elif modified == '#no#':
        result = {'removed': source}
    elif source == '#no#':
        result = {'added': modified}
    elif source != modified:
        if isinstance(source, dict) and isinstance(modified, dict):
            result = compare(source, modified)
        else:
            result = {
                'removed': source,
                'added': modified,
            }
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
