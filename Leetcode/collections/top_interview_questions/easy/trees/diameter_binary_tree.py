from typing import Optional

# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    rs = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def find_depth(node):
            if not node:
                return 0
            
            left = find_depth(node.left)
            right = find_depth(node.right)
            
            sm = left + right
            
            if sm > self.rs:
                self.rs = sm
            
            return max(left, right) + 1
        
        find_depth(root)
        return self.rs