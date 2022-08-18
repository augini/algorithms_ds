# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = deque([(root, root.val)])
        res = []

        while len(q):
            cur, mx_val = q.popleft()
            
            print(cur.val, mx_val)
            
            if cur.val >= mx_val:
                res.append(cur.val)
            
            if cur.left:
                if cur.left.val > mx_val:
                    q.append((cur.left, cur.left.val))
                else:
                    q.append((cur.left, mx_val))
                
            if cur.right:
                if cur.right.val > mx_val:
                    q.append((cur.right, cur.right.val))
                else:
                    q.append((cur.right, mx_val))
                    
        return len(res)
            