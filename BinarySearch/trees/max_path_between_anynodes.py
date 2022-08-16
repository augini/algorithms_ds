# https://binarysearch.com/problems/Largest-Tree-Sum-Path
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    mx = 0
    def solve(self, root):

        def post_order(node):
            if not node:
                return 0

            left  = post_order(node.left)
            right = post_order(node.right)

            cur_sum = left + right + node.val
            cur = max(cur_sum, node.val, left + node.val, right + node.val)

            if cur > self.mx:
                self.mx = cur

            return max(left, right) + node.val

        post_order(root)
        return self.mx
        