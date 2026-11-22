import pytest
from dsa_skelton.walk_middle import has_cycle, walk_middle

from dsa import to_linked


def _with_cycle(values, pos):
    # Build the list, then link the tail node back to the node at index pos.
    head = to_linked(values)
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    nodes[-1].next = nodes[pos]
    return head


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([1, 2, 3, 4, 5], 3, id="odd"),
        pytest.param([1, 2, 3, 4], 3, id="even"),  # even length -> upper middle
    ],
)
def test_walk_middle(values, expected):
    assert walk_middle(to_linked(values)) == expected


@pytest.mark.parametrize(
    "values, pos",
    [
        pytest.param([3, 2, 0, -4], 1, id="tail-to-index-1"),
        pytest.param([1, 2], 0, id="tail-to-head"),
    ],
)
def test_has_cycle_true(values, pos):
    assert has_cycle(_with_cycle(values, pos)) is True


@pytest.mark.parametrize(
    "values",
    [
        pytest.param([1], id="single"),
        pytest.param([], id="empty"),
    ],
)
def test_has_cycle_false(values):
    assert has_cycle(to_linked(values)) is False
