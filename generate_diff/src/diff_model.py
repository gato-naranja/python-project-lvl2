def make_add_node(value):
    node = make_node()
    node['diff'] = 'add'
    node['mod'] = ['added']
    node.pop('removed')
    node['added'] = value
    return node


def make_remove_node(value):
    node = make_node()
    node['diff'] = 'remove'
    node['mod'] = ['removed']
    node['removed'] = value
    node.pop('added')
    return node


def make_update_node(val_removed, val_added):
    node = make_node()
    node['diff'] = 'update'
    node['mod'] = ['removed', 'added']
    node['removed'] = val_removed
    node['added'] = val_added
    return node


def make_node():
    return {
        'diff': '',
        'mod': [],
        'added': '',
        'removed': '',
    }


def get_diff(elem):
    return elem.get('diff', 'next') if isinstance(elem, dict) else None


def get_mod(elem):
    return elem.get('mod') if isinstance(elem, dict) else None


def get_action(mod):
    return 'updated' if len(mod) > 1 else mod[0]
