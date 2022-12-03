# https://leetcode.com/problems/partition-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less, greater = ListNode(0), ListNode(0)
        curr = head

        head, greater_head = less, greater

        while curr:
            if curr.val < x:
                temp = curr
                curr = curr.next

                less.next = temp
                temp.next = None
                less = less.next

            elif curr.val >= x:
                temp = curr
                curr = curr.next

                greater.next = temp
                temp.next = None
                greater = greater.next

        less.next = greater_head.next
        return head.next
