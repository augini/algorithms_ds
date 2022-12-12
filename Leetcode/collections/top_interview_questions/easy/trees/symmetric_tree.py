# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class _Solution:
    def isSymmetric(self, root) -> bool:
        
        items = self.inorder(root, "root", [])
        _len = len(items)
        
        for i in range(_len // 2):
            c = _len - i-1
            if (items[i][0] != items[c][0]) or (items[i][1] == items[c][1]):
                return False
            
        return True
    
    def inorder(self, node, pos, col):
        if node.left:
            self.inorder(node.left, "l", col)

        col.append((node.val, pos))

        if node.right:
            self.inorder(node.right, "r", col)
            
        return col
        
class Solution:
    def isSymmetric(self, root) -> bool:
        if root == None:
            return True
        
        return self.check(root.left, root.right)
    
    def check(self, left, right):
        
        if left == None or right == None:
            return left == right

        if left.val != right.val:
            return False
        
        return self.check(left.right, right.left) and self.check(left.left, right.right)