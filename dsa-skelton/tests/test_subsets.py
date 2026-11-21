import pytest
from dsa_skelton.walk_subsets import walk_subsets


def _normalise(subsets):
    # Subset order and element order within a subset depend on the traversal,
    # so compare as a sorted list of sorted subsets
    # (a list, not a set, so duplicates count).
    return sorted(sorted(s) for s in subsets)


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([1, 2], [[], [1], [1, 2], [2]], id="small"),
        pytest.param([], [[]], id="empty"),
        pytest.param([5], [[], [5]], id="single"),
        pytest.param(
            [1, 2, 2],
            [[], [1], [1, 2], [1, 2], [1, 2, 2], [2], [2], [2, 2]],
            id="duplicates",
        ),
        pytest.param(
            [1, 2, 3, 4],
            [
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
            ],
            id="larger",
        ),
    ],
)
def test_walk_subsets(nums, expected):
    assert _normalise(walk_subsets(nums)) == expected
