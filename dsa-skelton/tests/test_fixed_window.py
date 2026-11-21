import pytest
from dsa_skelton.walk_fixed_window import walk_fixed_window


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        pytest.param([1, 2, 3, 4, 5], 3, [[1, 2, 3], [2, 3, 4], [3, 4, 5]], id="small"),
        pytest.param([], 1, [], id="empty"),
        pytest.param(
            [1, 2], 3, [], id="k-too-large"
        ),  # k larger than input -> no windows
        pytest.param([7], 1, [[7]], id="single"),
        pytest.param([2, 2, 2], 2, [[2, 2], [2, 2]], id="duplicates"),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8],
            4,
            [
                [1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6],
                [4, 5, 6, 7],
                [5, 6, 7, 8],
            ],
            id="larger",
        ),
    ],
)
def test_walk_fixed_window(nums, k, expected):
    assert walk_fixed_window(nums, k) == expected
