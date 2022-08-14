# https://binarysearch.com/problems/Linked-List-Delete-Last-Occurrence-of-Value

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, node, target):
        current = node
        prev = None

        while current:
            nxt = current.next
            current.next = prev

            prev = current
            current = nxt

        temp = prev
        # return prev
        cur = prev
        prev = None

        while cur:
            if cur.val == target:
                if prev:
                    prev.next = cur.next
                    cur.next = None
                else:
                    prev = cur.next
                    # cur.next = None
                    cur = prev

            # print(cur.val)
            prev = cur
            cur = cur.next

        return temp
     
sample = Solution()
root = LLNode(1)
root.next = LLNode(2)
root.next.next = LLNode(3)
root.next.next.next = LLNode(1)

print(sample.solve(root, 1))