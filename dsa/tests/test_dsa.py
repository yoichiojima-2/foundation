from dsa import TreeNode, to_linked, to_list, to_tree


def test_linked_roundtrip():
    assert to_list(to_linked([1, 2, 3])) == [1, 2, 3]
    assert to_list(to_linked([])) == []


def test_to_tree():
    root = to_tree([3, 9, 20, None, None, 15, 7])
    assert root == TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert to_tree([]) is None
    assert to_tree([1, None, 2]) == TreeNode(1, None, TreeNode(2))
