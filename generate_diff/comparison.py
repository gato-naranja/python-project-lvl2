def make_comparison(source_data, modified_data):
    return dict(
        map(
            lambda x:
            (x, get_value(source_data.get(x), modified_data.get(x))),
            set(source_data.keys()) | set(modified_data.keys())
        )
    )


def get_value(source_node, modified_node):
    if source_node == modified_node:
        return modified_node
    elif modified_node is None:
        return {'removed': source_node}
    elif source_node is None:
        return {'added': modified_node}
    elif source_node != modified_node:
        if isinstance(source_node, dict) and isinstance(modified_node, dict):
            return make_comparison(source_node, modified_node)
        else:
            return {
                'removed': source_node,
                'added': modified_node,
            }
