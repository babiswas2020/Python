class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None
  def reverse_level(self):
     stack=[]
     queue=[]
     queue.append(self)
     while queue:
         m=queue.pop(0)
         stack.append(m)
         if m.right:
            queue.append(m.right)
         if m.left:
            queue.append(m.left)
     while stack:
        print(stack.pop().value)

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
   node.insert(15)
   node.insert(26)
   node.insert(8)
   node.insert(10)
   node.insert(5)
   node.reverse_level()

    
   