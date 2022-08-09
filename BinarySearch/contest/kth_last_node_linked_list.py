# https://binarysearch.com/room/Empty-string-tAADCqx0B7?questionsetIndex=2


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # first approach is to get the length of the linked list
    # in the second iteration, get the k minus the length and return the value of the node at that point
     
    def _solve(self, node, k):
        size = 0
        current = node

        while current:
            size +=1
            current = current.next

        current = node
        steps = 0
        
        while current:
            steps+=1
            if size - steps == k:
                return current.val

            current = current.next

        return None
     
    # second solution is to use two pointers and have the first one ahead of the second by k nodes
    # so that when the ahead pointer reaches the end, the behind pointer is at the target node
    def solve(self, node, k):
        ahead, behind = node, node

        n = 0
        while n < k:
            ahead = ahead.next
            n+=1
        
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        
        return behind.val
   