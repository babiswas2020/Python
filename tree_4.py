class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

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

   def preorder(self):
       stack=[]
       stack.append(self)
       while stack:
           m=stack.pop()
           print(m.value)
           if m.right:
             stack.append(m.right)
           if m.left:
             stack.append(m.left)

if __name__=="__main__":
   node=Node(12)
   node.insert(6)
   node.insert(9)
   node.insert(4)
   node.insert(21)
   node.insert(15)
   node.insert(24)
   node.preorder()
