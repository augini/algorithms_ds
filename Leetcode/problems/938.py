# https://leetcode.com/problems/range-sum-of-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        stack = [root]
        _sum = 0

        while stack:
            curr = stack.pop()

            if curr.val >= low and curr.val <= high:
                _sum += curr.val

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)
        return _sum
