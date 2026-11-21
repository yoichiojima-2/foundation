import pytest
from dsa_skelton.walk_bfs import walk_bfs

from dsa import to_graph


# Adjacency dicts are built into GraphNodes; neighbours are visited in the
# order listed.
@pytest.mark.parametrize(
    "graph, start, expected",
    [
        pytest.param(
            {1: [2, 3], 2: [4], 3: [4, 5], 4: [6], 5: [6], 6: []},
            1,
            [1, 2, 3, 4, 5, 6],
            id="small",
        ),
        pytest.param({1: []}, 1, [1], id="single"),
        pytest.param(
            {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]},  # undirected, has cycles
            0,
            [0, 1, 2, 3],
            id="cycles",
        ),
        pytest.param(
            {1: [2], 2: [], 3: [1]},  # 3 is unreachable from 1
            1,
            [1, 2],
            id="unreachable",
        ),
        pytest.param(
            {
                1: [2, 3, 4],
                2: [5, 6],
                3: [6, 7],
                4: [8],
                5: [9],
                6: [9, 10],
                7: [10],
                8: [],
                9: [],
                10: [1],  # back edge to the start
            },
            1,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            id="larger",
        ),
    ],
)
def test_walk_bfs(graph, start, expected):
    assert walk_bfs(to_graph(graph)[start]) == expected
