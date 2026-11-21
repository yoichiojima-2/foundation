import pytest
from dsa_skelton.walk_hash import walk_hash


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([1, 2, 2, 3, 3, 3], {1: 1, 2: 2, 3: 3}, id="small"),
        pytest.param([], {}, id="empty"),
        pytest.param([5], {5: 1}, id="single"),
        pytest.param(
            [4, 1, 4, 2, 1, 4, 3, 2, 4],
            {4: 4, 1: 2, 2: 2, 3: 1},
            id="larger-duplicates",
        ),
    ],
)
def test_walk_hash(nums, expected):
    assert walk_hash(nums) == expected
