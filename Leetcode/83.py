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

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
