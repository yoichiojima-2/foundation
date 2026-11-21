import pytest
from dsa_skelton.walk_heap import walk_heap


@pytest.mark.parametrize(
    "items, expected",
    [
        pytest.param([5, 1, 4, 2, 3], [1, 2, 3, 4, 5], id="small"),
        pytest.param([], [], id="empty"),
        pytest.param([7], [7], id="single"),
        pytest.param([3, 1, 3, 2, 1], [1, 1, 2, 3, 3], id="duplicates"),
        pytest.param(
            [9, 4, 7, 1, 8, 2, 6, 3, 5, 0],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            id="larger",
        ),
    ],
)
def test_walk_heap(items, expected):
    assert walk_heap(items) == expected
