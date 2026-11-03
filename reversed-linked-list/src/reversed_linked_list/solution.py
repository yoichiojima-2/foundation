from dsa import ListNode


class Solution:
    def solution(self, head: ListNode | None) -> ListNode | None:
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
