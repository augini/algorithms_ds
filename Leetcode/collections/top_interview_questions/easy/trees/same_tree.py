from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def is_identical(p, q):
            if p is None or q is None:
                return p == q
            
            left = is_identical(p.left, q.left)
            right = is_identical(p.right, q.right)
            
            # print(left, right, p.val, q.val)
            
            if not left or not right:
                return False
            
            return p.val == q.val
        
        return is_identical(p, q)
        