import pytest
from dsa_skelton.walk_lower_bound import walk_lower_bound


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        pytest.param([1, 3, 5, 7], 5, 2, id="small-present"),
        pytest.param(
            [1, 3, 5, 7], 4, 2, id="small-absent"
        ),  # absent -> insertion point
        pytest.param([1, 3, 5, 7], 0, 0, id="below-all"),
        pytest.param([1, 3, 5, 7], 8, 4, id="above-all"),
        pytest.param([], 3, 0, id="empty"),
        pytest.param([5], 5, 0, id="single-present"),
        pytest.param([5], 6, 1, id="single-above"),
        pytest.param([1, 2, 2, 2, 3], 2, 1, id="duplicates"),
        pytest.param(list(range(0, 100, 3)), 50, 17, id="larger-absent"),
        pytest.param(list(range(0, 100, 3)), 51, 17, id="larger-present"),
        pytest.param(list(range(0, 100, 3)), 100, 34, id="larger-above-all"),
    ],
)
def test_walk_lower_bound(nums, target, expected):
    assert walk_lower_bound(nums, target) == expected
