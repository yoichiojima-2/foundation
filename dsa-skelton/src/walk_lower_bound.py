def walk_lower_bound(nums: list[int], target: int) -> int:
    """Return the first index i with nums[i] >= target in sorted nums (len(nums) if none)."""
    pass


NUMS1 = [1, 3, 5, 7]
NUMS2, TARGET2 = [], 3
NUMS3 = [5]
NUMS4, TARGET4 = [1, 2, 2, 2, 3], 2
NUMS5 = list(range(0, 100, 3))  # 0, 3, ..., 99


def test_small():
    assert walk_lower_bound(NUMS1, 5) == 2
    assert walk_lower_bound(NUMS1, 4) == 2  # absent -> insertion point


def test_bounds():
    assert walk_lower_bound(NUMS1, 0) == 0
    assert walk_lower_bound(NUMS1, 8) == 4


def test_empty():
    assert walk_lower_bound(NUMS2, TARGET2) == 0


def test_single():
    assert walk_lower_bound(NUMS3, 5) == 0
    assert walk_lower_bound(NUMS3, 6) == 1


def test_duplicates():
    assert walk_lower_bound(NUMS4, TARGET4) == 1


def test_larger():
    assert walk_lower_bound(NUMS5, 50) == 17
    assert walk_lower_bound(NUMS5, 51) == 17
    assert walk_lower_bound(NUMS5, 100) == 34
