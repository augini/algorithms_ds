# https://binarysearch.com/problems/Palindrome-Linked-List

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, node):

        if node is None:
            return True

        # get a pointer to the middle of the linked list
        slow, fast = node, node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse half of the list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # compare the left and right pointers
        curr = node
        while curr and prev:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next

        return True