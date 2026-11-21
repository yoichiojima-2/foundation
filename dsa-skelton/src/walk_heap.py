def walk_heap(items: list[int]) -> list[int]:
    """Push every item onto a min-heap, then pop until empty; return the pop order."""
    pass


ITEMS1 = [5, 1, 4, 2, 3]
ITEMS2 = []
ITEMS3 = [7]
ITEMS4 = [3, 1, 3, 2, 1]
ITEMS5 = [9, 4, 7, 1, 8, 2, 6, 3, 5, 0]


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
