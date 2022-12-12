# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/
from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    val = 0
    count = 0
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = 0
        self.count = 0
        
        def in_order(node):

            if node.left and not self.count == k:
                in_order(node.left)
            
            self.count+=1
            
            if self.count == k:
                self.val = node.val
            
            if node.right and not self.count == k:
                in_order(node.right)
        
        in_order(root)
        
        return self.val
        