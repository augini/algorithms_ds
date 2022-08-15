from collections import deque

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def _solve(self, root):
        if not root:
            return 0

        def get_depth(node):
            if not node:
                return 0
            
            left = get_depth(node.left)
            right = get_depth(node.right)

            return max(left, right) + 1
        
        max_depth = get_depth(root)
        sm = 0
        s = [(root, 1)]

        while len(s):
            cur, c_height = s.pop()
            if c_height == max_depth:
                sm+=cur.val

            if cur.left:
                s.append((cur.left, c_height+1))
            if cur.right:
                s.append((cur.right, c_height+1))

        return sm

    max_level, max_sum = 0, 0

    def solve(self, root):
        if root is None:
            return 0

        q = deque([(root, 0)])

        while len(q):
            cur, level = q.popleft()

            if level > self.max_level:
                self.max_level=level
                self.max_sum=cur.val
            else:
                self.max_sum+=cur.val

            if cur.left:
                q.append((cur.left, level+1))
            
            if cur.right:
                q.append((cur.right, level+1))
        
        return self.max_sum
        