class Node:
   def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

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

   def min(self):
      root=self
      while root.left!=None:
          root=root.left
      return root

   def search(self,value):
       temp=self
       while temp:
         if temp.value>value:
            temp=temp.left
         elif temp.value<value:
            temp=temp.right
         else:
            return temp
       return None

   def inorder_sucessor(self,node):
        if node.right:
           return self.min(node.right)
        else:
           temp1=self
           temp2=None
           while temp1:
              if temp1.value>node.value:
                 temp2=temp1
                 temp1=temp1.left
              elif temp1.value<node.value:
                 temp1=temp1.right
              else:
                 return temp2

if __name__=="__main__":
   node=Node(12)
   node.insert(21)
   node.insert(24)
   node.insert(18)
   node.insert(15)
   node.insert(20)
   node.insert(5)
   node.insert(7)
   node.insert(3)
   node.insert(1)
   node.insert(4)
   print("Printing inorder traversal")
   node.inorder()
   ptr=node.search(15)
   print("Printing the value of ptr")
   print(ptr.value)
   print("Inorder sucessor of the node is :")
   print(node.inorder_sucessor(ptr).value)
