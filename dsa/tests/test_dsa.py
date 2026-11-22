import pytest

from dsa import (
    DSU,
    TreeNode,
    to_cyclic_linked,
    to_graph,
    to_linked,
    to_list,
    to_tree,
)


def test_linked_roundtrip():
    assert to_list(to_linked([1, 2, 3])) == [1, 2, 3]
    assert to_list(to_linked([])) == []


def _nodes(head, n):
    # First n nodes by following next; never walks past n, so cycles are safe.
    nodes = []
    for _ in range(n):
        nodes.append(head)
        head = head.next
    return nodes


def test_to_cyclic_linked_tail_to_head():
    nodes = _nodes(to_cyclic_linked([1, 2, 3], 0), 3)
    assert [n.val for n in nodes] == [1, 2, 3]
    assert nodes[-1].next is nodes[0]


def test_to_cyclic_linked_tail_to_middle():
    nodes = _nodes(to_cyclic_linked([3, 2, 0, -4], 1), 4)
    assert [n.val for n in nodes] == [3, 2, 0, -4]
    assert nodes[-1].next is nodes[1]
    assert len({id(n) for n in nodes}) == 4  # no cycle before the tail


def test_to_cyclic_linked_self_loop():
    head = to_cyclic_linked([7], 0)
    assert head.val == 7
    assert head.next is head


@pytest.mark.parametrize(
    "values, pos",
    [
        pytest.param([], 0, id="empty"),
        pytest.param([1, 2], 2, id="pos-too-large"),
        pytest.param([1, 2], -1, id="negative-pos"),
    ],
)
def test_to_cyclic_linked_bad_pos(values, pos):
    with pytest.raises(IndexError):
        to_cyclic_linked(values, pos)


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


def test_dsu_starts_disjoint():
    dsu = DSU(3)
    assert [dsu.find(i) for i in range(3)] == [0, 1, 2]
    assert dsu.connected(1, 1)
    assert not dsu.connected(0, 1)


def test_dsu_union():
    dsu = DSU(5)
    assert dsu.union(0, 1) is True
    assert dsu.union(1, 2) is True
    assert dsu.union(0, 2) is False  # already in the same set
    assert dsu.union(3, 3) is False
    assert dsu.connected(0, 2)
    assert not dsu.connected(2, 3)
    assert len({dsu.find(i) for i in range(5)}) == 3


def test_dsu_union_by_size():
    dsu = DSU(4)
    dsu.union(0, 1)
    dsu.union(2, 0)  # smaller set {2} hangs under the root of {0, 1}
    assert dsu.find(2) == dsu.find(0) == 0
    assert dsu.size[0] == 3
    dsu.union(3, 2)
    assert dsu.find(3) == 0
    assert dsu.size[0] == 4


def test_dsu_path_compression():
    dsu = DSU(4)
    dsu.parent = [0, 0, 1, 2]  # chain 3 -> 2 -> 1 -> 0
    assert dsu.find(3) == 0
    assert dsu.parent == [0, 0, 0, 0]
