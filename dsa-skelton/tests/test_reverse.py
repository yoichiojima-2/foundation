import pytest
from dsa_skelton.walk_reverse import merge_two_lists, walk_reverse

from dsa import to_linked, to_list


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], id="small"),
        pytest.param([7], [7], id="single"),
    ],
)
def test_walk_reverse(values, expected):
    assert to_list(walk_reverse(to_linked(values))) == expected


def test_walk_reverse_empty():
    assert walk_reverse(None) is None


def test_walk_reverse_single_is_itself():
    # A single node is its own reversal: the same node comes back.
    head = to_linked([7])
    assert walk_reverse(head) is head


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4], id="small"),
        pytest.param([], [1, 3, 4], [1, 3, 4], id="left-empty"),
        pytest.param([1, 2, 4], [], [1, 2, 4], id="right-empty"),
    ],
)
def test_merge_two_lists(a, b, expected):
    assert to_list(merge_two_lists(to_linked(a), to_linked(b))) == expected
