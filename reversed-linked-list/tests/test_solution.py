import pytest
from reversed_linked_list.solution import Solution

from dsa import to_linked, to_list


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
        ([1, 1, 1], [1, 1, 1]),
        ([1, 2, 2, 3], [3, 2, 2, 1]),
    ],
)
def test_reverse_list(values, expected):
    head = to_linked(values)
    assert to_list(Solution().solution(head)) == expected
