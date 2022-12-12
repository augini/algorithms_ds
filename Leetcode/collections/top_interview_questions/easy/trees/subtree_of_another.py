from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot
        
        if self.is_identical(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def is_identical(self, p, q):
        if p is None or q is None:
            return p == q

        left = self.is_identical(p.left, q.left)
        right = self.is_identical(p.right, q.right)

        if not left or not right:
            return False

        return p.val == q.val
        