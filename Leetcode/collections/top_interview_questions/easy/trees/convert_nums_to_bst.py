# https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/631/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        
        return self.constructBinaryTree(nums, 0, len(nums)-1)
    
    def constructBinaryTree(self, nums, left, right):
        if (left > right):
            return None
        
        midpoint = left + (right-left) // 2
        node = TreeNode(nums[midpoint])
        
        node.left = self.constructBinaryTree(nums, left, midpoint-1)
        node.right = self.constructBinaryTree(nums, midpoint+1, right)
        
        return node