from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None


def to_linked(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_cyclic_linked(values: list[int], pos: int) -> ListNode:
    """Build a linked list whose tail links back to the node at index pos.

    pos == len(values) - 1 makes the tail point at itself. Raises IndexError
    unless 0 <= pos < len(values), so empty values always raise.
    """
    if not 0 <= pos < len(values):
        raise IndexError(f"pos {pos} out of range for {len(values)} values")
    nodes = [ListNode(v) for v in values]
    for node, nxt in zip(nodes, nodes[1:], strict=False):
        node.next = nxt
    nodes[-1].next = nodes[pos]
    return nodes[0]


def to_list(head: ListNode | None) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
