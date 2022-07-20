class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    max_sum = float("-inf")
    def solve(self, root):
        self.max_sum = float("-inf")
        self.postorder(root)
        return self.max_sum
     
    def postorder(self, root):
       if root is not None:
          if root.left:
             left_node = self.postorder(root.left)
             
          if root.right:
             right_node = self.postorder(root.right)
             
          if root.left is None and root.right is None:
             return {"isBst": True, "max": root.val, "min": root.val, "sum": root.val}
          
          if root.left is None:
             return {"isBst": True, "max": root.right.val, "min": root.val, "sum": root.val + root.right.val}
          
          if left_node["isBst"] and right_node["isBst"]:
             if left_node["max"] < root.val and root.val < right_node["min"]:
                current_sum = left_node["sum"] + right_node["sum"] + root.val
                
                if current_sum > self.max_sum:
                   self.max_sum = current_sum
                   
                return {"isBst": True, "max": right_node["max"], "min": left_node["min"], "sum": current_sum}
             
             elif left_node["max"] > root.val or root.val > right_node["min"]:
                return {"isBst": False}
             
          
# example = Tree(1)
# example.left = Tree(5)
# example.right = Tree(3)
# example.left.left = Tree(6)
# example.left.right = Tree(7)
# example.right.left = Tree(2)
# example.right.right = Tree(4)

example = Tree(0)
example.right = Tree(1)

sample = Solution()
print(sample.solve(example))