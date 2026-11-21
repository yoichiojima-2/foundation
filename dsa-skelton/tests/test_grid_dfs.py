from dsa_skelton.walk_grid_dfs import (
    GRID1,
    GRID2,
    GRID3,
    GRID4,
    GRID5,
    walk_grid_dfs,
)


def _copy(grid):
    # Pass a copy so solutions that mark visited cells in place
    # don't alter the constants.
    return [row[:] for row in grid]


def test_small():
    assert walk_grid_dfs(_copy(GRID1)) == [(0, 0), (0, 1), (1, 1), (2, 2)]


def test_empty():
    assert walk_grid_dfs(_copy(GRID2)) == []


def test_all_water():
    assert walk_grid_dfs(_copy(GRID3)) == []


def test_single():
    assert walk_grid_dfs(_copy(GRID4)) == [(0, 0)]


def test_larger():
    assert walk_grid_dfs(_copy(GRID5)) == [
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
    ]
