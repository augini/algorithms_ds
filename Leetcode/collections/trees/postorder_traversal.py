# Definition for a binary tree node.

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        # first stack to traverse the tree
        stack = deque([root])

        # second stack to keep track
        q = deque([])

        while stack:
            node = stack.pop()
            q.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        while q:
            result.append(q.pop())

        return result

    def postorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        def postorder(node: Optional[TreeNode]):

            if node.left:
                postorder(node.left)

            if node.right:
                postorder(node.right)

            result.append(node.val)

        postorder(root)

        return result
