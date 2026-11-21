def walk_hash(nums: list[int]) -> dict[int, int]:
    """Count occurrences of each value in nums."""
    pass


NUMS1 = [1, 2, 2, 3, 3, 3]
NUMS2 = []
NUMS3 = [5]
NUMS4 = [4, 1, 4, 2, 1, 4, 3, 2, 4]


def test_small():
    assert walk_hash(NUMS1) == {1: 1, 2: 2, 3: 3}


def test_empty():
    assert walk_hash(NUMS2) == {}


def test_single():
    assert walk_hash(NUMS3) == {5: 1}


def test_larger_duplicates():
    assert walk_hash(NUMS4) == {4: 4, 1: 2, 2: 2, 3: 1}
