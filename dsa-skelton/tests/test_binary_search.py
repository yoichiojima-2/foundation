from dsa_skelton.walk_binary_search import (
    NUMS1,
    NUMS2,
    NUMS3,
    NUMS4,
    NUMS5,
    NUMS6,
    TARGET1,
    TARGET2,
    TARGET3,
    TARGET4,
    TARGET5,
    TARGET6_HIT,
    TARGET6_MISS,
    walk_binary_search,
)


def test_small():
    assert walk_binary_search(NUMS1, TARGET1) == 3


def test_empty():
    assert walk_binary_search(NUMS2, TARGET2) == -1


def test_single():
    assert walk_binary_search(NUMS3, TARGET3) == 0


def test_absent():
    assert walk_binary_search(NUMS4, TARGET4) == -1


def test_duplicates():
    # Any index holding the target is correct; which one depends on the midpoints taken.
    assert walk_binary_search(NUMS5, TARGET5) in {1, 2, 3}


def test_larger():
    assert walk_binary_search(NUMS6, TARGET6_HIT) == 17
    assert walk_binary_search(NUMS6, TARGET6_MISS) == -1
