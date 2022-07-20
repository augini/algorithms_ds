# problem: https://binarysearch.com/problems/Binary-Tree-to-Linked-List

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, root):
        
        if root is None:
            return None

        rlist = self.inorder(root, [])

        result = None

        for item in rlist:
            if result is None:
                result = LLNode(item)
                last = result
            else:
                last.next = LLNode(item)
                last = last.next
        
        return result

    def inorder(self, root, rlist):
        if root is not None:
            if root.left:
                self.inorder(root.left, rlist)

            rlist.append(root.val)

            if root.right:
                self.inorder(root.right, rlist)

            return rlist
                
        