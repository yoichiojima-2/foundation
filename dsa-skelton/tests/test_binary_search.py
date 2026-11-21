import pytest
from dsa_skelton.walk_binary_search import walk_binary_search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        pytest.param([1, 3, 5, 7, 9, 11], 7, 3, id="small"),
        pytest.param([], 3, -1, id="empty"),
        pytest.param([5], 5, 0, id="single"),
        pytest.param([1, 3, 5], 4, -1, id="absent"),
        pytest.param(list(range(0, 100, 3)), 51, 17, id="larger-hit"),
        pytest.param(list(range(0, 100, 3)), 50, -1, id="larger-miss"),
    ],
)
def test_walk_binary_search(nums, target, expected):
    assert walk_binary_search(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target, valid",
    [
        # Any index holding the target is correct;
        # which one depends on the midpoints taken.
        pytest.param([1, 2, 2, 2, 3], 2, {1, 2, 3}, id="duplicates"),
    ],
)
def test_walk_binary_search_any_match(nums, target, valid):
    assert walk_binary_search(nums, target) in valid
