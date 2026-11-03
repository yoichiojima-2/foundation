import pytest
from binary_tree_level_order_traversal.solution import Solution

from dsa import to_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2], [[1], [2]]),
        ([1, None, 2], [[1], [2]]),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([1, 2, None, 3, None, 4], [[1], [2], [3], [4]]),
        ([1, 2, 3, None, 4, None, 5], [[1], [2, 3], [4, 5]]),
    ],
)
def test_level_order(values, expected):
    assert Solution().solution(to_tree(values)) == expected
