from dsa_skelton.walk_two_pointers import walk_two_pointers

NUMS1 = [1, 2, 3, 4, 5]  # odd length: middle element is never paired
NUMS2 = []
NUMS3 = [7]
NUMS4 = [1, 1, 2, 2]
NUMS5 = [1, 2, 3, 4, 5, 6, 7, 8]


def test_small():
    assert walk_two_pointers(NUMS1) == [(1, 5), (2, 4)]


def test_empty():
    assert walk_two_pointers(NUMS2) == []


def test_single():
    assert walk_two_pointers(NUMS3) == []


def test_duplicates():
    assert walk_two_pointers(NUMS4) == [(1, 2), (1, 2)]


def test_larger():
    assert walk_two_pointers(NUMS5) == [(1, 8), (2, 7), (3, 6), (4, 5)]
