# https://leetcode.com/problems/linked-list-cycle-ii/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define slow, fast pointers
        slow, fast = head, head

        # start traversing the list
        # detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # no cycle in the list, return -1
        if not fast or not fast.next:
            return None

        # have another pointer start from the beginning of the list
        check = head

        while check != slow:
            check = check.next
            slow = slow.next

        return check
