class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def inorder(node):
   if node:
      if node.left:
         inorder(node.left)
      print(node.value)
      if node.right:
         inorder(node.right)


def insert(node,value):
   if node.value>value:
      if node.left:
         insert(node.left,value)
      else:
         node.left=Node(value)
   elif node.value<value:
      if node.right:
         insert(node.right,value)
      else:
         node.right=Node(value)
   else:
      print("Duplication not allowed")
     

def find_distance(root,x):
    dist1=dist2=-1
    if not root:
       return -1
    elif root==x:
       return 0
    else:
       dist1=find_distance(root.left,x)
       dist2=find_distance(root.right,x)
       if dist1>0:
          return 1+dist1
       elif dist2>0:
          return 1+dist2
       else:
          return -1

if __name__=="__main__":
  node=Node(12)
  insert(node,21)
  insert(node,18)
  insert(node,23)
  insert(node,6)
  insert(node,4)
  insert(node,8)
  insert(node,1)
  insert(node,5)
  inorder(node)
  print(find_distance(node,node.left.left))

  
