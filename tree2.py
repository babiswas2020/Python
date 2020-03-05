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
       node=self
       while node!=None:
           if node.left==None:
              print(node.value)
              node=node.right
           else:
              curr=node.left
              while curr.right!=node and curr.right:
                  curr=curr.right
              if curr.right==node:
                 curr.right=None
                 node=node.right
              else:
                 curr.right=node
                 print(curr.value)
                 node=node.left

if __name__=="__main__":
   node=Node(12)
   node.insert(21)
   node.insert(25)
   node.insert(18)
   node.insert(6)
   node.insert(8)
   node.insert(9)
   node.preorder()

                 

              
              