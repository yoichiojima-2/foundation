import pytest
from dsa_skelton.walk_two_pointers import walk_two_pointers


@pytest.mark.parametrize(
    "nums, expected",
    [
        # odd length: middle element is never paired
        pytest.param([1, 2, 3, 4, 5], [(1, 5), (2, 4)], id="small"),
        pytest.param([], [], id="empty"),
        pytest.param([7], [], id="single"),
        pytest.param([1, 1, 2, 2], [(1, 2), (1, 2)], id="duplicates"),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8],
            [(1, 8), (2, 7), (3, 6), (4, 5)],
            id="larger",
        ),
    ],
)
def test_walk_two_pointers(nums, expected):
    assert walk_two_pointers(nums) == expected
