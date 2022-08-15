# https://binarysearch.com/problems/Vertical-Lines-in-Binary-Tree

from collections import defaultdict

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    hd = defaultdict(int)

    def solve(self, root):
        self.hd = defaultdict(int)
        
        def in_order(node, d):
            if node.left:
                in_order(node.left, d-1)
            
            self.hd[d]+=1

            if node.right:
                in_order(node.right, d+1)

        in_order(root, 0)
        return len(list(self.hd.values()))
        