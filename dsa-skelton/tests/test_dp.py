import pytest
from dsa_skelton.walk_dp import walk_dp


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(5, [0, 1, 1, 2, 3, 5], id="small"),
        pytest.param(0, [0], id="zero"),
        pytest.param(1, [0, 1], id="one"),
        pytest.param(
            15,
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610],
            id="larger",
        ),
    ],
)
def test_walk_dp(n, expected):
    assert walk_dp(n) == expected
