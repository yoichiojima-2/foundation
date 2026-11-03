import pytest
from reversed_linked_list.solution import ListNode, Solution


def to_linked(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


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
