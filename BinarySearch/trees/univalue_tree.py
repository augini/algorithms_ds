# https://binarysearch.com/room/Kadane's-Room-XCwwzSTaWX?questionsetIndex=3

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    item = 0

    def solve(self, root, val = None):
        if not root:
            return True
        
        if not val:
            val = root.val
        
        if root.val != val:
            return False
        
        return self.solve(root.left, val) and self.solve(root.right, val)