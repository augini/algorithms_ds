# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        first, second = head, head

        while first and first.next:
            first = first.next.next
            second = second.next

        return second
