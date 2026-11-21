import pytest
from dsa_skelton.walk_variable_window import walk_variable_window


# Inputs are non-negative, so shrinking always lowers the sum.
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        pytest.param(
            [1, 2, 3, 4, 5], 6, [[1], [1, 2], [1, 2, 3], [4], [5]], id="small"
        ),
        pytest.param([], 5, [], id="empty"),
        # single element larger than k -> window shrinks to empty
        pytest.param([9], 5, [[]], id="single-exceeds-k"),
        pytest.param([3, 3, 3, 3], 6, [[3], [3, 3], [3, 3], [3, 3]], id="duplicates"),
        pytest.param(
            [2, 1, 5, 1, 3, 2, 4, 1],
            7,
            [
                [2],
                [2, 1],
                [1, 5],
                [1, 5, 1],
                [1, 3],
                [1, 3, 2],
                [2, 4],
                [2, 4, 1],
            ],
            id="larger",
        ),
    ],
)
def test_walk_variable_window(nums, k, expected):
    assert walk_variable_window(nums, k) == expected
