from generate_diff.src.diff_model import make_remove_node
from generate_diff.src.diff_model import make_add_node
from generate_diff.src.diff_model import make_update_node


def make_comparison(first_data, second_data):
    all_items = set(first_data.keys()) | set(second_data.keys())
    unique_items = set(first_data.keys()) ^ set(second_data.keys())
    shared_items = set(first_data.keys()) & set(second_data.keys())
    result_diff = {}
    for item in all_items:
        if item in unique_items:
            if item in first_data.keys():
                result_diff[item] = make_remove_node(first_data[item])
            elif item in second_data.keys():
                result_diff[item] = make_add_node(second_data[item])
        if item in shared_items:
            if first_data[item] == second_data[item]:
                result_diff[item] = first_data[item]
            elif first_data[item] != second_data[item]:
                if is_dict(first_data[item]) and is_dict(second_data[item]):
                    result_diff[item] = make_comparison(
                        first_data[item],
                        second_data[item]
                        )
                else:
                    result_diff[item] = make_update_node(
                        first_data[item],
                        second_data[item],
                    )
    return result_diff


def is_dict(value):
    return isinstance(value, dict)
