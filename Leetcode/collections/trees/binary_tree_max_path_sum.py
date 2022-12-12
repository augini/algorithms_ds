# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_path = -float("inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -float("inf")
        
        def traverse(node):
            if not node:
                return 0
            
            left = traverse(node.left)
            right = traverse(node.right)
            

            including_node = left + right + node.val
            paths = max(node.val, left+node.val, right+node.val)
            
            current = max(including_node, paths)
            
            if current > self.max_path:
                self.max_path = current
                
            return paths
        
        traverse(root)
        
        return self.max_path
        