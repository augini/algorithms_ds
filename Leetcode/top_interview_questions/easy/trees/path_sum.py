# Definition for a binary tree node.
# https://leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        
        if not root:
            return False
        
        stack = [(root, root.val)]
        
        while len(stack) > 0:
            
            node, cur_sum = stack.pop()

            if node.left is not None:
                left_sum = cur_sum + node.left.val
                stack.append((node.left, left_sum))
                
            if node.right is not None:
                right_sum = cur_sum + node.right.val
                stack.append((node.right, right_sum))
           
            if cur_sum == targetSum and node.left is None and node.right is None:
                return True
            
        return False