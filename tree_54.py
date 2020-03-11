class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def find_max(node):
   max1=max2=0
   if not node:
      return -1
   else:
      res=node.value
      if node.left:
         max1=find_max(node.left)
      if node.right:
         max2=find_max(node.right)
      if res<max1:
         res=max1
      if res<max2:
         res=max2
      return res

if __name__=="__main__":
   node=Node(12)
   node.left=Node(21)
   node.right=Node(14)
   node.left.left=Node(16)
   node.left.right=Node(19)
   node.right.left=Node(23)
   node.right.right=Node(17)
   print(find_max(node))



      
       