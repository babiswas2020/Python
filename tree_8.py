class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def level_order_trav(self):
       queue=[]
       queue.append(self)
       while queue:
           m=queue.pop(0)
           print(m.value)
           if m.left:
              queue.append(m.left)
           if m.right:
              queue.append(m.right)

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
   node.insert(25)
   node.insert(5)
   node.insert(9)
   node.insert(1)
   node.level_order_trav()

   
   

