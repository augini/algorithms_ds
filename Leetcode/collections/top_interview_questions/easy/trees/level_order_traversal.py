# Definition for a binary tree node.
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        
        if root == None:
            return []
        
        _queue = deque([(root, 0)])
        
        result = defaultdict(list)
        
        while len(_queue) > 0:
            current, level = _queue.popleft()
            
            if current.left:
                _queue.append((current.left, level + 1))
                
            result[level].append(current.val)
            
            if current.right:
                _queue.append((current.right, level + 1))
                
        return result.values()
        