import pytest
from valid_parentheses.solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("([)]", False),
        ("{[]}", True),
        (")", False),
        ("(()", False),
        ("([{}])", True),
        ("][", False),
        ("(((((((((()))))))))", False),
    ]
)
def test_valid_parentheses(s, expected):
    assert Solution().solution(s) == expected