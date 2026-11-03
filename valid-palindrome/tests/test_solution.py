import pytest
from valid_palindrome.solution import Solution


@pytest.mark.parametrize("s, expected", [("a man, a plan, a canal: panama", True), ("race a car", False)])
def test_solution(s, expected):
    assert Solution().solution(s) == expected
