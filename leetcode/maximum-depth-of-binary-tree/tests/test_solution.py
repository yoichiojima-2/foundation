import pytest
from maximum_depth_of_binary_tree.solution import Solution

from dsa import to_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([1, 2, None, 3, None, 4], 4),
        ([1, None, 2, None, 3, None, 4], 4),
    ],
)
def test_max_depth(values, expected):
    assert Solution().solution(to_tree(values)) == expected
