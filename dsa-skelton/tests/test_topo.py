import pytest
from dsa_skelton.walk_topo import walk_topo


# Every node appears as a key; graph[u] lists the nodes u points to.
@pytest.mark.parametrize(
    "graph, expected",
    [
        pytest.param({}, [], id="empty"),
        pytest.param({1: []}, [1], id="single"),
        pytest.param(
            {1: [2], 2: [3], 3: []}, [1, 2, 3], id="chain"
        ),  # only one valid order
    ],
)
def test_walk_topo_unique(graph, expected):
    assert walk_topo(graph) == expected


@pytest.mark.parametrize(
    "graph",
    [
        pytest.param({5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}, id="small"),
        pytest.param(
            {1: [2, 3], 2: [4], 3: [4, 5], 4: [6], 5: [6], 6: [7], 7: [], 8: [5]},
            id="larger-branching",
        ),
    ],
)
def test_walk_topo_valid(graph):
    # Topological order is not unique, so check it is a valid one:
    # same nodes (sorted comparison) and every edge points forward.
    order = walk_topo(graph)
    assert sorted(order) == sorted(graph)
    pos = {node: i for i, node in enumerate(order)}
    for u, vs in graph.items():
        for v in vs:
            assert pos[u] < pos[v], f"edge {u}->{v} out of order in {order}"
