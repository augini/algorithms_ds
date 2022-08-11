# https://binarysearch.com/problems/Longest-Tree-Path

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    mx = 0
    def solve(self, root):
        if not root:
            return 0

        def traverse(node):
            if node is None:
                return 0
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            curr = left+right+1
            if curr > self.mx:
                self.mx = curr

            return max(left, right) + 1
        
        traverse(root)
        return self.mx