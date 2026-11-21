import pytest
from dsa_skelton.walk_dfs import walk_dfs

from dsa import to_graph


# Adjacency dicts are built into GraphNodes; leaves map to []. The walk
# starts at the root.
@pytest.mark.parametrize(
    "tree, node, expected",
    [
        pytest.param(
            {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []},
            1,
            [1, 2, 4, 5, 3, 6],
            id="small",
        ),
        pytest.param({1: []}, 1, [1], id="single"),
        pytest.param(
            {
                1: [2, 3, 4],
                2: [5, 6],
                3: [],
                4: [7, 8, 9],
                5: [10],
                6: [],
                7: [],
                8: [11, 12],
                9: [],
                10: [],
                11: [],
                12: [],
            },
            1,
            [1, 2, 5, 10, 6, 3, 4, 7, 8, 11, 12, 9],
            id="larger-branching",
        ),
    ],
)
def test_walk_dfs(tree, node, expected):
    assert walk_dfs(to_graph(tree)[node]) == expected
