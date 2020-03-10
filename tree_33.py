import sys

class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def min(root):
  if root==None:
     return None
  while root.left:
      root=root.left
  return root

def inorder_sucessor(root,target):
    temp1=temp2=None
    if root==None:
      return None
    elif root==target:
       return min(root.right)
    elif root.left==target:
       return root
    elif target==max(root.right):
         return None
    else:
      temp1=inorder_sucessor(root.right,target)    
      temp2=inorder_sucessor(root.left,target)
      if temp1:
         return temp1
      elif temp2:
         return temp2
      else:
         return None

def find_node(node,x):
   if not node:
      return node
   else:
     if node.value==x:
        return node
     else:
        right=find_node(node.right,x)
        left=find_node(node.left,x)
        if right:
           return right
        elif left:
           return left
        else:
           return None

       

if __name__=="__main__":
   node=Node(12)
   node.left=Node(21)
   node.right=Node(18)
   node.left.right=Node(15)
   node.left.left=Node(11)
   node.right.right=Node(10)
   node.right.left=Node(23)
   node.left.right.left=Node(20)
   node.left.right.right=Node(16)
   node.left.left.right=Node(17)
   ptr=find_node(node,int(sys.argv[1]))
   print("printing ptr value")
   print(ptr.value)
   print(inorder_sucessor(node,ptr).value)


