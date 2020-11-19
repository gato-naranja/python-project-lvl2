def compare(source_data, modified_data):
    return dict(
        map(
            lambda x: (
                x,
                collect_diff_values(source_data.get(x), modified_data.get(x))
                ),
            set(source_data.keys()) | set(modified_data.keys())
        )
    )


def collect_diff_values(source, modified):
    if source == modified:
        result = modified
    elif modified is None:
        result = {'removed': source}
    elif source is None:
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
