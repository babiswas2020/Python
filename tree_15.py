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
       root=self
       stack=[]
       while True:
          if root:
             stack.append(root)
             root=root.left
          else:
             if not stack:
               break
             else:
               if stack[-1].right==None:
                  root=stack.pop()
                  print(root.value)
                  while root==stack[-1].right:
                      root=stack.pop()
                      print(root.value)
                      if not stack:
                         break
               if stack:
                 root=stack[-1].right
               else:
                 root=None

if __name__=="__main__":
   node=Node(12)
   node.insert(21)
   node.insert(18)
   node.insert(24)
   node.insert(27)
   node.insert(22)
   node.insert(6)
   node.insert(9)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   node.postorder()

                  
               
              
             