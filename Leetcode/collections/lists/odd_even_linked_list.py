# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # traverse the list and store the even nodes in the new list
        # temp, temp2, counter = head, None, 1
        # newList = ListNode(0, None)
        # even = newList

        head_even, odd, even = head.next, head, head.next

        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next

        odd.next = head_even
        return head

    def oddEvenList_(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # traverse the list and store the even nodes in the new list
        temp, temp2, counter = head, None, 1
        newList = ListNode(0, None)
        even = newList

        while temp:
            if counter % 2 == 0:
                even.next = temp

                temp = temp.next
                temp2.next = temp

                even.next.next = None

                even = even.next
            else:
                temp2 = temp
                temp = temp.next

            counter += 1

        temp2.next = newList.next

        return head
