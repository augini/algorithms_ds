# Definition for singly-linked list.
from collections import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # get a pointer to the first, middle, last nodes in the list
        second, first = head, head

        while first and first.next:
            first = first.next

            if first.next:
                first = first.next
                second = second.next
            # print(first.val, second.val)

        # reverse the second portion of the list
        back, reverser = second, second.next

        while reverser:
            temp = reverser
            reverser = reverser.next
            temp.next = back

            back = temp

        second.next = None

        # reorder the list based on those pointers and prev property
        start, end = head, first

        while end and start:
            temp = start
            start = start.next

            end_temp = end
            end = end.next

            end_temp.next = None
            temp.next = end_temp

            end_temp.next = start

        return head
