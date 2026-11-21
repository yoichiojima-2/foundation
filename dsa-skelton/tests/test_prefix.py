import pytest
from dsa_skelton.walk_prefix import walk_prefix


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([1, 2, 3, 4], [0, 1, 3, 6, 10], id="small"),
        pytest.param([], [0], id="empty"),
        pytest.param([5], [0, 5], id="single"),
        pytest.param([2, 2, 2], [0, 2, 4, 6], id="duplicates"),
        pytest.param(
            [3, -1, 3, -1, 0, 2, 5, -4],
            [0, 3, 2, 5, 4, 4, 6, 11, 7],
            id="larger",
        ),
    ],
)
def test_walk_prefix(nums, expected):
    assert walk_prefix(nums) == expected
