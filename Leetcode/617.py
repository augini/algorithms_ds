# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if not root1:
            return root2
        if not root2:
            return root1

        result = root1
        stack1, stack2 = [root1], [root2]

        while stack1 and stack2:
            curr1, curr2 = stack1.pop(), stack2.pop()
            curr1.val = curr1.val + curr2.val

            if curr2.left:
                if curr1.left:
                    stack1.append(curr1.left)
                    stack2.append(curr2.left)
                else:
                    curr1.left = curr2.left

            if curr2.right:
                if curr1.right:
                    stack1.append(curr1.right)
                    stack2.append(curr2.right)
                else:
                    curr1.right = curr2.right

        return result
