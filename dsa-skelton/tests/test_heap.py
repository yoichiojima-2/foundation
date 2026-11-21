from dsa_skelton.walk_heap import (
    ITEMS1,
    ITEMS2,
    ITEMS3,
    ITEMS4,
    ITEMS5,
    walk_heap,
)


def test_small():
    assert walk_heap(ITEMS1) == [1, 2, 3, 4, 5]


def test_empty():
    assert walk_heap(ITEMS2) == []


def test_single():
    assert walk_heap(ITEMS3) == [7]


def test_duplicates():
    assert walk_heap(ITEMS4) == [1, 1, 2, 3, 3]


def test_larger():
    assert walk_heap(ITEMS5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
