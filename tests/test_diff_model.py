from generate_diff.src.diff_model import make_add_node
from generate_diff.src.diff_model import make_remove_node
from generate_diff.src.diff_model import make_update_node
from generate_diff.src.diff_model import get_diff, get_mod, get_action


def test_add_node():
    val = 123456
    assert make_add_node(val) == {
        'diff': 'add',
        'mod': ['added'],
        'added': val,
    }


def test_remove_node():
    val = 'abcd'
    assert make_remove_node(val) == {
        'diff': 'remove',
        'mod': ['removed'],
        'removed': val,
    }


def test_update_node():
    val_remove = 123456
    val_add = 'abcd'
    node = make_update_node(val_remove, val_add)
    assert node == {
        'diff': 'update',
        'mod': ['removed', 'added'],
        'removed': val_remove,
        'added': val_add,
    }


def test_get_diff():
    node = make_add_node('abcd')
    node_simple = {'key': 'simple_value'}
    simple_value = 'abcde'
    assert get_diff(node) == 'add'
    assert get_diff(node_simple) == 'next'
    assert get_diff(simple_value) is None


def test_get_mod():
    node = make_add_node('abcd')
    simple = 'simple_value'
    assert get_mod(node) == ['added']
    assert get_diff(simple) is None


def test_get_action():
    val_remove = 123456
    val_add = 'abcd'
    node_update = make_update_node(val_remove, val_add)
    node_add = make_add_node(val_add)
    node_remove = make_remove_node(val_remove)
    assert get_action(node_update['mod']) == 'updated'
    assert get_action(node_add['mod']) == 'added'
    assert get_action(node_remove['mod']) == 'removed'
