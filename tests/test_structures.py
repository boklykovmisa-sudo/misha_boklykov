import pytest
from structures.array import DynamicArray
from structures.linked_list import LinkedList
from structures.deque import Deque
from structures.avl_tree import AVLTree, height


def test_array():
    array = DynamicArray()
    array.append(10)
    array.append(20)
    assert len(array) == 2
    assert array.get(0) == 10
    assert array.remove_at(0) == 10
    assert array.get(0) == 20


def test_linked_list():
    linked = LinkedList()
    for value in [1, 2, 3]:
        linked.append(value)
    assert linked.to_list() == [1, 2, 3]
    assert linked.remove(2)
    assert linked.to_list() == [1, 3]
    assert not linked.remove(99)


def test_deque():
    deque = Deque()
    deque.append_left(2)
    deque.append_left(1)
    deque.append_right(3)
    assert deque.pop_left() == 1
    assert deque.pop_right() == 3
    assert len(deque) == 1
    assert deque.pop_left() == 2
    with pytest.raises(IndexError):
        deque.pop_left()


def test_avl_tree():
    tree = AVLTree()
    for value in [30, 20, 10, 25, 40, 50, 45]:
        tree.insert(value)
    assert tree.inorder() == [10, 20, 25, 30, 40, 45, 50]
    assert tree.contains(25)
    assert not tree.contains(100)

    def check_balance(node):
        if node is None:
            return
        assert abs(height(node.left) - height(node.right)) <= 1
        check_balance(node.left)
        check_balance(node.right)

    check_balance(tree.root)


@pytest.mark.parametrize('values', [[1, 2, 3], [3, 2, 1], [10, 20, 30, 40], [5, 5, 5]])
def test_avl_insertion_orders(values):
    tree = AVLTree()
    for value in values:
        tree.insert(value)
    assert tree.inorder() == sorted(set(values))
