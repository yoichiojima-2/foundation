import pytest
from dsa_skelton.walk_next_greater import daily_temperatures, walk_next_greater


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([2, 1, 2, 4, 3], [4, 2, 4, -1, -1], id="small"),
        pytest.param([5, 4, 3, 2, 1], [-1, -1, -1, -1, -1], id="strictly-decreasing"),
    ],
)
def test_walk_next_greater(nums, expected):
    assert walk_next_greater(nums) == expected


@pytest.mark.parametrize(
    "temps, expected",
    [
        pytest.param(
            [73, 74, 75, 71, 69, 72, 76, 73],
            [1, 1, 4, 2, 1, 1, 0, 0],
            id="small",
        ),
    ],
)
def test_daily_temperatures(temps, expected):
    assert daily_temperatures(temps) == expected
