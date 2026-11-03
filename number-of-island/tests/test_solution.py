import pytest
from number_of_island.solution import Solution


def make_grid(rows):
    return [list(row) for row in rows]


@pytest.mark.parametrize(
    "rows, expected",
    [
        (["11110", "11010", "11000", "00000"], 1),
        (["11000", "11000", "00100", "00011"], 3),
        ([], 0),
        (["0"], 0),
        (["1"], 1),
        (["000", "000"], 0),
        (["111", "111"], 1),
        (["10", "01"], 2),
        (["101", "010", "101"], 5),
        (["1111"], 1),
        (["1", "1", "1"], 1),
        (["1010"], 2),
        (["111", "101", "111"], 1),
        (["1010", "0101", "1010"], 6),
        (["10", "10", "01", "01", "10"], 3),
    ],
)
def test_num_islands(rows, expected):
    assert Solution().solution(make_grid(rows)) == expected
