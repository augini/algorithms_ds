# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        first, second = head, head
        head = head.next
        temp = None

        while first and first.next:
            first = first.next

            second.next = first.next
            first.next = second

            if temp:
                temp.next = first

            temp = second

            second = second.next
            first = second

            if second and not second.next:
                break

            temp.next = None

        # print(first.val, second.val)
        return head
