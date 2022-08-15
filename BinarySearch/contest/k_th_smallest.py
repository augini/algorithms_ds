# https://binarysearch.com/room/Leaf-Village-yyOFMnkJM8?questionsetIndex=1

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = []

    def solve(self, root, k):
        self.result = []
        def k_smallest(node):
            if node.left:
                k_smallest(node.left)

            self.result.append(node.val)

            if node.right:
                k_smallest(node.right)

        k_smallest(root)
        return self.result[k]
        