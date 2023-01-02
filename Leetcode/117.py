# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

from typing import Optional
from collections import deque

# Definition for a Node
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:

        if not root:
            return root

        stack = deque([(root, 0)])
        prev = (None, 0)

        while stack:
            curr, level = stack.popleft()

            if prev[0] and prev[1] == level:
                prev[0].next = curr
            else:
                curr.next = None

            if curr.left:
                stack.append((curr.left, level + 1))

            if curr.right:
                stack.append((curr.right, level + 1))

            prev = (curr, level)
        return root
