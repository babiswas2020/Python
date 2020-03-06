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

   def postorder(self):
       stack1=[]
       stack2=[]
       stack1.append(self)
       while stack1:
           m=stack1.pop()
           stack2.append(m)
           if m.left:
             stack1.append(m.left)
           if m.right:
             stack1.append(m.right)
       while stack2:
          print(stack2.pop().value)

if __name__=="__main__":
   node=Node(12)
   node.insert(21)
   node.insert(24)
   node.insert(18)
   node.insert(6)
   node.insert(9)
   node.insert(4)
   node.postorder()


           
       