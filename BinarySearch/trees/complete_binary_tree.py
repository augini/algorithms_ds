from collections import deque

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root):
        if root is None:
            return True

        q=deque([root])
        flag = False

        while len(q):
            current = q.popleft()
            if current is None:
                flag = True
            else:
                if flag:
                    return False
                q.append(current.left)
                q.append(current.right)
        
        return True