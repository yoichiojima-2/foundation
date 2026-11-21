import pytest
from dsa_skelton.walk_grid_dfs import walk_grid_dfs


@pytest.mark.parametrize(
    "grid, expected",
    [
        pytest.param(
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 0, 1],
            ],
            [(0, 0), (0, 1), (1, 1), (2, 2)],
            id="small",
        ),
        pytest.param([], [], id="empty"),
        pytest.param(
            [
                [0, 0],
                [0, 0],
            ],
            [],
            id="all-water",
        ),
        pytest.param([[1]], [(0, 0)], id="single"),
        pytest.param(
            [
                [1, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 0, 1],
            ],
            [
                (0, 0),
                (1, 0),
                (0, 1),
                (0, 4),
                (1, 4),
                (1, 3),
                (2, 2),
                (3, 2),
                (3, 1),
                (3, 0),
                (3, 4),
            ],
            id="larger",
        ),
    ],
)
def test_walk_grid_dfs(grid, expected):
    assert walk_grid_dfs(grid) == expected
