# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count=0

    def solve(self, root):
        if root is None:
            return 0

        _left, _right = None, None

        if root.left:
            _left = self.solve(root.left)
        if root.right:
            _right = self.solve(root.right)

        if _left is None and _right is not None:
            self.count +=1
        
        if _right is None and _left is not None:
            self.count +=1
        
        return self.count
