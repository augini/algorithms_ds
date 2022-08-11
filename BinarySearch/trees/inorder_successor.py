# https://binarysearch.com/problems/Inorder-Successor

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root, t):
        def find_min(node):
            curr = node

            while curr:
                if curr.left is None:
                    break
                curr = curr.left

            return curr.val
        
        def search(node, t):
            curr = node
            succ = Tree(None)

            while node:
                if curr.val < t:
                    curr = curr.right
                elif curr.val > t:
                    succ = curr
                    curr = curr.left
                else:
                    break
            return succ.val

        stack = [root]

        while len(stack):
            curr = stack.pop()

            if curr.left:
                stack.append(curr.left)

            if curr.val == t:
                if curr.right:
                    return find_min(curr.right)
                else:
                    return search(root, t)
                    
            if curr.right:
                stack.append(curr.right)