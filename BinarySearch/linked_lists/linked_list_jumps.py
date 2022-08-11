# https://binarysearch.com/problems/Linked-List-Jumps

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, node):
        head = node

        while node:
            steps = node.val

            for i in range(1, steps):
                if node.next:
                    node.next = node.next.next
                else:
                    break
            node = node.next
        return head
        