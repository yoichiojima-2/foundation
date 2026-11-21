from dsa_skelton.walk_fixed_window import (
    K1,
    K2,
    K3,
    K4,
    K5,
    K6,
    NUMS1,
    NUMS2,
    NUMS3,
    NUMS4,
    NUMS5,
    NUMS6,
    walk_fixed_window,
)


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
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7],
        [5, 6, 7, 8],
    ]
