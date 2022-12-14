# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root

        values = []

        def inorder(node, replace):
            if node.left:
                inorder(node.left, replace)

            if replace == True:
                node.val = values.pop()
            elif replace == False:
                values.append(node.val)

            if node.right:
                inorder(node.right, replace)

        inorder(root, False)

        values.sort(reverse=True)

        inorder(root, True)

        return root
