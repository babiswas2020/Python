class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
      if self:
        if self.left:
           self.left.postorder()
        if self.right:
           self.right.postorder()
        print(self.value)

   def preorder(self):
      if self:
        print(self.value)
        if self.left:
           self.left.preorder()
        if self.right:
           self.right.preorder()

   def inorder(self):
      if self:
         if self.left:
            self.left.inorder()
         print(self.value)
         if self.right:
            self.right.inorder()

   def insert(self,value):
      if self.value>value:
        if self.left:
            self.left.insert(value)
        else:
            self.left=Node(value)
      elif self.value<value:
        if self.right:
           self.right.insert(value)
        else:
           self.right=Node(value)
      else:
         print("Duplication not allowed")

if __name__=="__main__":
   node=Node(12)
   node.insert(18)
   node.insert(8)
   node.insert(21)
   node.insert(14)
   node.insert(4)
   node.insert(10)
   print("Printing inorder traversal:")
   node.inorder()
   print("Printing preorder traversal:")
   node.preorder()
   print("Postorder traversal")
   node.postorder()



