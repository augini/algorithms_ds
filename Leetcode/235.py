# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        def findNode(curr, node):
            q = deque([root])
            nodes, values = [], []

            while q:
                curr = q.popleft()

                values.append(curr.val)
                nodes.append(curr)

                # if value is found, return values and nodes
                if curr.val == node.val:
                    return (values, nodes)

                # use the bst properties

                # if target is larger, go right
                if node.val > curr.val:
                    q.append(curr.right)

                # if target is small, go left
                if node.val < curr.val:
                    q.append(curr.left)

        # find p
        pValues, pNodes = findNode(root, p)
        # find q
        qValues = findNode(root, q)

        # get the list length
        lp, lq = len(pValues), len(qValues)

        for i in range(lp - 1, -1, -1):
            for j in range(lq - 1, -1, -1):
                if pValues[i] == qValues[j]:
                    return pNodes[i]

        return None
