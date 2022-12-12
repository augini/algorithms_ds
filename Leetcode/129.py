# Definition for a binary tree node.
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root

        sums = []
        stack = [(root, "")]

        while stack:
            curr = stack.pop()
            node, val = curr

            curr_sum = val + str(node.val)

            if not node.left and not node.right:
                sums.append(curr_sum)

            if node.left:
                stack.append((node.left, curr_sum))

            if node.right:
                stack.append((node.right, curr_sum))

        for i in range(len(sums)):
            sums[i] = int(sums[i])

        return sum(sums)
