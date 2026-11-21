from dsa_skelton.walk_prefix import (
    NUMS1,
    NUMS2,
    NUMS3,
    NUMS4,
    NUMS5,
    walk_prefix,
)


def test_small():
    assert walk_prefix(NUMS1) == [0, 1, 3, 6, 10]


def test_empty():
    assert walk_prefix(NUMS2) == [0]


def test_single():
    assert walk_prefix(NUMS3) == [0, 5]


def test_duplicates():
    assert walk_prefix(NUMS4) == [0, 2, 4, 6]


def test_larger():
    assert walk_prefix(NUMS5) == [0, 3, 2, 5, 4, 4, 6, 11, 7]
