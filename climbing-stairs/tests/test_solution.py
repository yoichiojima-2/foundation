import pytest
from climbing_stairs.solution import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (10, 89),
        (20, 10946),
        (30, 1346269),
        (45, 1836311903),
    ],
)
def test_climb_stairs(n, expected):
    assert Solution().solution(n) == expected
