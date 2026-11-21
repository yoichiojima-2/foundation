from dsa_skelton.walk_bfs import (
    GRAPH1,
    GRAPH2,
    GRAPH3,
    GRAPH4,
    GRAPH5,
    walk_bfs,
)


def test_small():
    assert walk_bfs(GRAPH1, 1) == [1, 2, 3, 4, 5, 6]


def test_single():
    assert walk_bfs(GRAPH2, 1) == [1]


def test_cycles():
    assert walk_bfs(GRAPH3, 0) == [0, 1, 2, 3]


def test_unreachable():
    assert walk_bfs(GRAPH4, 1) == [1, 2]


def test_larger():
    assert walk_bfs(GRAPH5, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
