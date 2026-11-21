def walk_topo(graph: dict[int, list[int]]) -> list[int]:
    """Return a topological order of the DAG (edge u -> v means u comes before v)."""
    pass


# Every node appears as a key; graph[u] lists the nodes u points to.
GRAPH1 = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}
GRAPH2 = {}
GRAPH3 = {1: []}
GRAPH4 = {1: [2], 2: [3], 3: []}  # a chain has exactly one valid order
GRAPH5 = {1: [2, 3], 2: [4], 3: [4, 5], 4: [6], 5: [6], 6: [7], 7: [], 8: [5]}


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
