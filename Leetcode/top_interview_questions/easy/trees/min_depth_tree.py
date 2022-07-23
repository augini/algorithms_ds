# Definition for a binary tree node.
# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root) -> int:
        
        if not root:
            return 0
        
        _left = self.minDepth(root.left)
        _right = self.minDepth(root.right)
        
        
        if (_left == 0 and _right is not 0) or (_left is not 0 and _right == 0):
            return max(_left, _right) + 1
        
        return min(_left, _right) + 1