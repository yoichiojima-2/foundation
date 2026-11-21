from dsa_skelton.walk_variable_window import (
    K1,
    K2,
    K3,
    K4,
    K5,
    NUMS1,
    NUMS2,
    NUMS3,
    NUMS4,
    NUMS5,
    walk_variable_window,
)


def test_small():
    assert walk_variable_window(NUMS1, K1) == [[1], [1, 2], [1, 2, 3], [4], [5]]


def test_empty():
    assert walk_variable_window(NUMS2, K2) == []


def test_single_exceeds_k():
    assert walk_variable_window(NUMS3, K3) == [[]]


def test_duplicates():
    assert walk_variable_window(NUMS4, K4) == [[3], [3, 3], [3, 3], [3, 3]]


def test_larger():
    assert walk_variable_window(NUMS5, K5) == [
        [2],
        [2, 1],
        [1, 5],
        [1, 5, 1],
        [1, 3],
        [1, 3, 2],
        [2, 4],
        [2, 4, 1],
    ]
