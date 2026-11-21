from dsa_skelton.walk_topo import (
    GRAPH1,
    GRAPH2,
    GRAPH3,
    GRAPH4,
    GRAPH5,
    walk_topo,
)


def _assert_topo(order, graph):
    # Topological order is not unique, so check it is a valid one:
    # same nodes (sorted comparison) and every edge points forward.
    assert sorted(order) == sorted(graph)
    pos = {node: i for i, node in enumerate(order)}
    for u, vs in graph.items():
        for v in vs:
            assert pos[u] < pos[v], f"edge {u}->{v} out of order in {order}"


def test_small():
    _assert_topo(walk_topo(GRAPH1), GRAPH1)


def test_empty():
    assert walk_topo(GRAPH2) == []


def test_single():
    assert walk_topo(GRAPH3) == [1]


def test_chain():
    assert walk_topo(GRAPH4) == [1, 2, 3]


def test_larger_branching():
    _assert_topo(walk_topo(GRAPH5), GRAPH5)
