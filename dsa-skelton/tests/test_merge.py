import pytest
from dsa_skelton.walk_merge import walk_merge


@pytest.mark.parametrize(
    "intervals, expected",
    [
        pytest.param(
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
            id="small",
        ),
        pytest.param(
            [[8, 10], [15, 18], [2, 6], [1, 3]],
            [[1, 6], [8, 10], [15, 18]],
            id="unsorted",
        ),
        pytest.param([[1, 4], [4, 5]], [[1, 5]], id="touching"),
        pytest.param([[1, 10], [2, 3]], [[1, 10]], id="nested"),
    ],
)
def test_walk_merge(intervals, expected):
    assert walk_merge(intervals) == expected
