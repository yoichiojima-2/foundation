import pytest
from dsa_skelton.walk_dijkstra import network_delay, walk_dijkstra


# Every node appears as a key; graph[u] lists (neighbour, weight) pairs.
@pytest.mark.parametrize(
    "graph, start, expected",
    [
        pytest.param(
            {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []},
            0,
            {0: 0, 1: 3, 2: 1, 3: 4},
            id="small",
        ),
    ],
)
def test_walk_dijkstra(graph, start, expected):
    assert walk_dijkstra(graph, start) == expected


@pytest.mark.parametrize(
    "times, n, k, expected",
    [
        pytest.param([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2, id="small"),
        pytest.param([[1, 2, 1]], 2, 2, -1, id="unreachable"),
    ],
)
def test_network_delay(times, n, k, expected):
    assert network_delay(times, n, k) == expected
