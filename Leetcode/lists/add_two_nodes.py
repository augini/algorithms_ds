# Definition for singly-linked list.
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        result = ListNode(0, None)
        pointer = result
        remainder = 0

        while l1 or l2:
            res = 0

            if l1 and l2:
                res = l1.val + l2.val
            elif l1:
                res = l1.val
            elif l2:
                res = l2.val

            if remainder != 0:
                res += remainder

            if res >= 10:
                remainder = res // 10
                res = res % 10
            else:
                remainder = 0

            newNode = ListNode(res, None)

            pointer.next = newNode
            pointer = pointer.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if remainder:
            newNode = ListNode(remainder, None)
            pointer.next = newNode

        return result.next
