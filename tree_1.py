class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

   def inorder(self):
      root=self
      if root==None:
         return
      else:
          while root:
             if root.left==None:
                print(root.value)
                root=root.right
             else:
                curr=root.left
                while curr.right!=root and curr.right:
                     curr=curr.right
                if curr.right==root:
                   curr.right=None
                   print(root.value)
                   root=root.right
                else:
                   curr.right=root
                   root=root.left

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
   node.insert(21)
   node.insert(17)
   node.insert(19)
   node.insert(16)
   node.insert(24)
   node.insert(22)
   node.insert(26)
   node.insert(6)
   node.insert(10)
   node.insert(3)
   node.insert(5)
   node.inorder()
