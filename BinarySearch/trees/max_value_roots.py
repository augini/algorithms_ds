# https://binarysearch.com/problems/Counting-Maximal-Value-Roots-in-Binary-Tree

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    counter = 0

    def solve(self, root):
        self.postorder(root)
        return self.counter

    def postorder(self, node):

        if node is None:
            return -math.inf

        _left = self.postorder(node.left)
        _right = self.postorder(node.right)

        max_sub = max(_left, _right)

        if max_sub <= node.val:
            self.counter+=1
            return node.val
        
        return max_sub

