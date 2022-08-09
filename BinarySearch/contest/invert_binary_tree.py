# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        if root is None:
            return None

        def in_order_invert(node):
            if node.left:
                in_order_invert(node.left)
            if node.right:
                in_order_invert(node.right)
            
            temp = node.left
            node.left = node.right
            node.right = temp
        
        in_order_invert(root)

        return root
        