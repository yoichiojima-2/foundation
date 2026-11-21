import pytest
from dsa_skelton.walk_stack import walk_stack


@pytest.mark.parametrize(
    "items, expected",
    [
        pytest.param([1, 2, 3], [3, 2, 1], id="small"),
        pytest.param([], [], id="empty"),
        pytest.param([7], [7], id="single"),
        pytest.param([1, 2, 2, 3, 1], [1, 3, 2, 2, 1], id="duplicates"),
        pytest.param(list(range(10)), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], id="larger"),
    ],
)
def test_walk_stack(items, expected):
    assert walk_stack(items) == expected
