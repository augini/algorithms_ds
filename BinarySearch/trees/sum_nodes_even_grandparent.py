# https://binarysearch.com/problems/Sum-of-Nodes-with-Even-Grandparent-Values
from collections import deque
import copy

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root):

        _deque = deque([ (root, []) ])
        counter = 0

        while len(_deque) > 0:
            node, ancestry = _deque.popleft()
            ancestry = copy.deepcopy(ancestry)

            if len(ancestry) > 2:
                ancestry.pop(0)

            if node.left:
                _deque.append((node.left, ancestry))

            if node.right:
                _deque.append((node.right, ancestry))

            if len(ancestry) == 2 and ancestry[0] % 2 == 0:
                counter+=node.val

            ancestry.append(node.val)
        return counter