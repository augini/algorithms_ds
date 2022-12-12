# https://leetcode.com/problems/binary-tree-right-side-view/submissions/
from typing import Optional, List
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        hash_map = defaultdict(int)
        q = deque([(root, 0)])
        
        while len(q):
            cur, level = q.popleft()
            
            hash_map[level]=cur.val
            
            if cur.left:
                q.append((cur.left, level+1))
            
            if cur.right:
                q.append((cur.right, level+1))
                
        return list(hash_map.values())
        