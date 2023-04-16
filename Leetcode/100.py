from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_identical(p, q):
            if p is None or q is None:
                return p == q

            left = is_identical(p.left, q.left)
            right = is_identical(p.right, q.right)

            if not left or not right:
                return False

            return p.val == q.val

        return is_identical(p, q)

    def _isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return q == q

        def is_identical(node_1, node_2):
            if node_1.val == node_2.val:
                left, right = False, False

                if node_1.left and node_2.left:
                    left = is_identical(node_1.left, node_2.left)

                elif not node_1.left and not node_2.left:
                    left = True

                if node_1.right and node_2.right:
                    right = is_identical(node_1.right, node_2.right)

                elif not node_1.right and not node_2.right:
                    right = True

                return left and right

            return False

        return is_identical(p, q)
