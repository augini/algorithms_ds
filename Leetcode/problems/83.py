from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        first, second = head.next, head

        while first:

            if first.val == second.val:

                while first and first.val == second.val:
                    temp = first
                    first = first.next

                temp.next = None
                second.next = first

            if first:
                first = first.next
                second = second.next

        return head
