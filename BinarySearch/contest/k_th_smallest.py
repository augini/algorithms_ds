# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        result = []
        def pre_order(node):
            if node.left:
                pre_order(node.left)

            result.append(node.val)

            if node.right:
                pre_order(node.right)

        pre_order(root)
        
        return result[k]