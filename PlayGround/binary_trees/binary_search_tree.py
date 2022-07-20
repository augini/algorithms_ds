class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        
        if self.left is not None:
            self.left.inorder(vals)
            
        if self.val is not None:
            vals.append(self.val)
        
        if self.right is not None:
            self.right.inorder(vals)
            
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
      
binary_tree = BSTNode()

# binary_tree.insert(12)
# binary_tree.insert(7)
# binary_tree.insert(10)
# binary_tree.insert(5)
# binary_tree.insert(4)


class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
    
  def insert(self, value):
    if not self.value:
      self.value = value
      return
    
    if self.value == value:
      return
    
    if value < self.value:
      if self.left is None:
        self.left = TreeNode(value)
      else:
        self.left.insert(value)
        
    elif value > self.value:
      if self.right is None:
        self.right = TreeNode(value)
        
      else:
        self.right.insert(value)
        
  def inorder(self):
      if self.left:
        self.left.inorder()
      
      print(self.value)
      
      if self.right:
        self.right.inorder()
        
  def preorder(self):
    if self.value:
      print(self.value)
      
    if self.left:
      self.left.preorder()
    
    if self.right:
      self.right.preorder()
      
  def postorder(self):
    if self.left:
      self.left.preorder()
    
    if self.right:
      self.right.preorder()
      
    if self.value:
      print(self.value)
      
  def find(self, value):
    if value < self.value:
      if self.left is None:
        return False
      else:
        return self.left.find(value)
        
    elif value > self.value:
      
      if self.right is None:
        return False
      
      else:
        return self.right.find(value)
      
    return True
      
      
        
bs_tree = TreeNode(10)

bs_tree.insert(12)
bs_tree.insert(5)
bs_tree.insert(4)
bs_tree.insert(30)
bs_tree.insert(10)

# print(bs_tree.right.right.value)
# bs_tree.inorder()
# bs_tree.preorder()

print(bs_tree.find(3))