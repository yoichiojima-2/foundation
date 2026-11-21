from dsa_skelton.walk_stack import (
    ITEMS1,
    ITEMS2,
    ITEMS3,
    ITEMS4,
    ITEMS5,
    walk_stack,
)


def test_small():
    assert walk_stack(ITEMS1) == [3, 2, 1]


def test_empty():
    assert walk_stack(ITEMS2) == []


def test_single():
    assert walk_stack(ITEMS3) == [7]


def test_duplicates():
    assert walk_stack(ITEMS4) == [1, 3, 2, 2, 1]


def test_larger():
    assert walk_stack(ITEMS5) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
