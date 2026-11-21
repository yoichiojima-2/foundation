from dsa_skelton.walk_subsets import (
    NUMS1,
    NUMS2,
    NUMS3,
    NUMS4,
    NUMS5,
    walk_subsets,
)


def _normalise(subsets):
    # Subset order and element order within a subset depend on the traversal,
    # so compare as a sorted list of sorted subsets
    # (a list, not a set, so duplicates count).
    return sorted(sorted(s) for s in subsets)


def test_small():
    assert _normalise(walk_subsets(NUMS1)) == [[], [1], [1, 2], [2]]


def test_empty():
    assert _normalise(walk_subsets(NUMS2)) == [[]]


def test_single():
    assert _normalise(walk_subsets(NUMS3)) == [[], [5]]


def test_duplicates():
    assert _normalise(walk_subsets(NUMS4)) == [
        [],
        [1],
        [1, 2],
        [1, 2],
        [1, 2, 2],
        [2],
        [2],
        [2, 2],
    ]


def test_larger():
    assert _normalise(walk_subsets(NUMS5)) == [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 4],
        [1, 3],
        [1, 3, 4],
        [1, 4],
        [2],
        [2, 3],
        [2, 3, 4],
        [2, 4],
        [3],
        [3, 4],
        [4],
    ]
