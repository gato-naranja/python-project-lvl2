def make_node(obligatory_value, ext_value='', mod=''):
    if mod == 'add':
        node = {
            'diff': 'added',
            'major': obligatory_value,
        }
    elif mod == 'remove':
        node = {
            'diff': 'removed',
            'minor': obligatory_value,
        }
    elif mod == 'change':
        node = {
            'diff': 'updated',
            'from': obligatory_value,
            'to': ext_value,
        }
    else:
        node = obligatory_value
    return node


def is_dict(item):
    return isinstance(item, dict)


def sort_comparison_result(in_data):
    sorted_data = {}
    for key in sorted(in_data.keys()):
        if isinstance(in_data[key], dict):
            sorted_data[key] = sort_comparison_result(in_data[key])
        else:
            sorted_data[key] = in_data[key]
    return sorted_data


def make_comparsion(first_data, second_data):
    unic_keys = set(first_data.keys()) ^ set(second_data.keys())
    result_diff = {}
    for key in unic_keys:
        if key in first_data.keys():
            result_diff[key] = make_node(first_data[key], mod='remove')
        elif key in second_data.keys():
            result_diff[key] = make_node(second_data[key], mod='add')
    shared_keys = set(first_data.keys()).intersection(set(second_data.keys()))
    for key in shared_keys:
        if first_data[key] == second_data[key]:
            result_diff[key] = make_node(first_data[key])
        elif first_data[key] != second_data[key]:
            if is_dict(first_data[key]) and is_dict(second_data[key]):
                children = make_comparsion(first_data[key], second_data[key])
                result_diff[key] = make_node(children)
            else:
                result_diff[key] = make_node(
                    first_data[key],
                    second_data[key],
                    mod='change')
    return sort_comparison_result(result_diff)
