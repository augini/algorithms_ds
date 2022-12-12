# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # return head if k == 0 or only has only one node
        if not head or k == 0 or not head.next:
            return head

        # get the total length of the list and round the k if it is longer than the length
        temp, length = head, 0
        while temp:
            temp = temp.next
            length += 1
        k = k % length

        # again return 0 if the k is 0 after the round up
        if k == 0:
            return head

        # divide the list into two parts based on the length
        first, second, steps = head, head, 0
        while steps < k:
            first = first.next
            steps += 1

        while first and first.next:
            first = first.next
            second = second.next

        # append the second list to the end of the first list
        new_head = second.next
        second.next = None
        first.next = head

        return new_head
