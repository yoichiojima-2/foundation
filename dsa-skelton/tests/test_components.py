import pytest
from dsa_skelton.walk_components import count_provinces, walk_components


@pytest.mark.parametrize(
    "n, unions, expected",
    [
        pytest.param(5, [(0, 1), (1, 2), (3, 4)], 2, id="small"),
        pytest.param(4, [], 4, id="no-unions"),
        pytest.param(4, [(0, 1), (1, 2), (2, 3)], 1, id="all-connected"),
    ],
)
def test_walk_components(n, unions, expected):
    assert walk_components(n, unions) == expected


@pytest.mark.parametrize(
    "is_connected, expected",
    [
        pytest.param([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2, id="small"),
        pytest.param([[1, 0], [0, 1]], 2, id="disconnected"),
        pytest.param([[1]], 1, id="single"),
    ],
)
def test_count_provinces(is_connected, expected):
    assert count_provinces(is_connected) == expected
