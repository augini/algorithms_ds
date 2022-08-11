# https://binarysearch.com/problems/Linked-List-to-Integer

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, node):

        curr = node
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr = prev
        result, dg = 0, 0
        while curr:
            if curr.val != 0:
                result += 2**dg
            curr = curr.next
            dg+=1
        return result
        