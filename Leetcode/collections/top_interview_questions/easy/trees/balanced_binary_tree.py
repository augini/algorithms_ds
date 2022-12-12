# https://leetcode.com/problems/balanced-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        
        return self.checkBalanced(root)[0]
    
    
    def checkBalanced(self, node):
        if not node:
            return [True, 0]
        
        _left = self.checkBalanced(node.left)
        _right = self.checkBalanced(node.right)
        
        
        balanced = _left[0] and _right[0]
        diff = _left[1] - _right[1]
        
        depth = max(_left[1], _right[1]) + 1
        
        if abs(diff) > 1 or not balanced:
            return [False, depth]
        
        return [True, depth]