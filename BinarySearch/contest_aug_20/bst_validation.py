# https://binarysearch.com/problems/Binary-Search-Tree-Validation

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def solve(self, root):

        def check_bst(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return check_bst(node.left, left, node.val) and check_bst(node.right, node.val, right)
        
        return check_bst(root, -float("inf"), float("inf"))
        