from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None


class Solution:
    def solution(self, head):
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
