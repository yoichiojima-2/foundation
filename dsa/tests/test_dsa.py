from dsa import TreeNode, to_graph, to_linked, to_list, to_tree


def test_linked_roundtrip():
    assert to_list(to_linked([1, 2, 3])) == [1, 2, 3]
    assert to_list(to_linked([])) == []


def test_to_tree():
    root = to_tree([3, 9, 20, None, None, 15, 7])
    assert root == TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert to_tree([]) is None
    assert to_tree([1, None, 2]) == TreeNode(1, None, TreeNode(2))


def test_to_graph():
    nodes = to_graph({1: [2, 3], 2: [1], 3: []})
    assert [n.val for n in nodes[1].neighbors] == [2, 3]
    assert nodes[1].neighbors[0] is nodes[2]
    assert nodes[2].neighbors[0] is nodes[1]  # cycle shares the same node
    assert repr(nodes[2]) == "GraphNode(2, neighbors=[1])"
    assert to_graph({}) == {}
    assert list(to_graph({1: [4]})) == [1, 4]  # neighbour-only node is created
