# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:

        # get the total length of the list
        total = 0
        temp = head

        while temp:
            total += 1
            temp = temp.next

        # determine how many pieces will be in each part
        each_k = total // k
        remainder = total % k
        steps = [each_k] * k

        i = 0
        while remainder > 0:
            steps[i] = steps[i] + 1
            remainder -= 1
            i += 1

        temp = head
        curr, i = 1, 0
        result = []

        # divide the list into k parts according to predefined steps
        while temp:
            if curr == steps[i]:
                pointer = temp
                temp = temp.next

                pointer.next = None
                result.append(head)

                head = temp
                curr = 1
                i += 1
            else:
                temp = temp.next
                curr += 1

        length = len(steps)
        while i < length:
            result.append(None)
            i += 1

        return result
        # print(each_k, total, remainder, steps)
