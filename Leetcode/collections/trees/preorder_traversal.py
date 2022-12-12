# Definition for a binary tree node.
from typing import Optional
from collections import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        stack = [root]

        while stack:
            curr = stack.pop()

            result.append(curr.val)

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)

        return result

    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        def preorder(node: Optional[TreeNode]):
            result.append(node.val)

            if node.left:
                preorder(node.left)

            if node.right:
                preorder(node.right)

        preorder(root)

        return result
