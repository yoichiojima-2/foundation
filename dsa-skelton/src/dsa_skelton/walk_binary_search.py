def walk_binary_search(nums: list[int], target: int) -> int:
    """Return an index of target in sorted nums, or -1 if absent."""
    pass


NUMS1, TARGET1 = [1, 3, 5, 7, 9, 11], 7
NUMS2, TARGET2 = [], 3
NUMS3, TARGET3 = [5], 5
NUMS4, TARGET4 = [1, 3, 5], 4  # absent
NUMS5, TARGET5 = [1, 2, 2, 2, 3], 2
NUMS6 = list(range(0, 100, 3))  # 0, 3, ..., 99
TARGET6_HIT, TARGET6_MISS = 51, 50


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
