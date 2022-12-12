# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_path = -float("inf")

    def _maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -float("inf")

        def traverse(node):
            if not node:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            including_node = left + right + node.val
            paths = max(node.val, left + node.val, right + node.val)

            current = max(including_node, paths)

            if current > self.max_path:
                self.max_path = current

            return paths

        traverse(root)

        return self.max_path

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        if not root or (not root.left and not root.right):
            return root.val

        def traverse(node):

            if not node:
                return 0

            left_sum = traverse(node.left)
            right_sum = traverse(node.right)

            # print(left_sum, right_sum, node.val)
            curr_sum = left_sum + right_sum + node.val

            temp_max = max(
                node.val, left_sum + node.val, right_sum + node.val, curr_sum
            )

            if temp_max > self.max_path:
                self.max_path = temp_max

            return max(left_sum + node.val, right_sum + node.val, node.val)

        traverse(root)

        return self.max_path
