from dsa_skelton.walk_dfs import (
    TREE1,
    TREE2,
    TREE3,
    walk_dfs,
)


def test_small():
    assert walk_dfs(TREE1, 1, []) == [1, 2, 4, 5, 3, 6]


def test_single():
    assert walk_dfs(TREE2, 1, []) == [1]


def test_subtree():
    assert walk_dfs(TREE1, 2, []) == [2, 4, 5]


def test_larger_branching():
    assert walk_dfs(TREE3, 1, []) == [1, 2, 5, 10, 6, 3, 4, 7, 8, 11, 12, 9]
