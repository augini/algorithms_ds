# https://binarysearch.com/problems/Tree-with-Distinct-Parities

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    counter = 0

    def solve(self, root):
        self.check(root)
        return self.counter
    
    def check(self, node):

        if not node:
            return (0, False)

        _left = self.check(node.left)
        _right = self.check(node.right)


        if _left[1] and _right[1] and (_left[0] + _right[0]) % 2 == 1:
                self.counter +=1

        _sum = _left[0] + _right[0] + node.val

        return (_sum, True)  