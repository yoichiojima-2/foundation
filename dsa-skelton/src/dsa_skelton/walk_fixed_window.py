def walk_fixed_window(nums: list[int], k: int):
    """Return every contiguous window of width k, left to right, as lists."""
    pass


NUMS1, K1 = [1, 2, 3, 4, 5], 3
NUMS2, K2 = [], 1
NUMS3, K3 = [1, 2], 3  # k larger than input -> no windows
NUMS4, K4 = [7], 1
NUMS5, K5 = [2, 2, 2], 2
NUMS6, K6 = [1, 2, 3, 4, 5, 6, 7, 8], 4


def test_small():
    assert walk_fixed_window(NUMS1, K1) == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]


def test_empty():
    assert walk_fixed_window(NUMS2, K2) == []


def test_k_too_large():
    assert walk_fixed_window(NUMS3, K3) == []


def test_single():
    assert walk_fixed_window(NUMS4, K4) == [[7]]


def test_duplicates():
    assert walk_fixed_window(NUMS5, K5) == [[2, 2], [2, 2]]


def test_larger():
    assert walk_fixed_window(NUMS6, K6) == [
        [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8],
    ]
