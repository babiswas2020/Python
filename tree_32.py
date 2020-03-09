import sys

class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None


def find_node(node,x):
   if node==None:
      return None
   else:
      if node.value==x:
        return node
      else:
         temp1=find_node(node.left,x)
         temp2=find_node(node.right,x)
         if temp1:
            return temp1
         elif temp2:
            return temp2
         else:
            return None

def inorder(node):
    if node:
       if node.left:
          inorder(node.left)
       print(node.value)
       if node.right:
          inorder(node.right)
          

def max(node):
   root=node
   while root.right!=None:
       root=root.right
   return root

def min(node):
    root=node
    while root.left!=None:
          root=root.left
    return root

def find_sucessor(node,x):
    if node==None:
      return None
    else:
      if node.left==x:
         return node
      temp1=find_sucessor(node.left,x)
      temp2=find_sucessor(node.right,x)
      if temp1:
        return temp1
      elif temp2:
        return temp2
      else:
        return None

def inorder_sucessor(node,x):
    root=node
    if x.right!=None:
       ptr=min(x.right)
       return ptr
    elif node==x:
       return None
    else:
       ptr=max(node.right)
       if x==ptr:
         return None
       else:
         ptr=find_sucessor(node,x)
         return ptr

if __name__=="__main__":
   node=Node(12)
   node.left=Node(21)
   node.left.right=Node(18)
   node.left.left=Node(24)
   node.left.right.left=Node(15)
   node.left.right.right=Node(20)
   node.right=Node(6)
   node.right.left=Node(2)
   node.right.right=Node(10)
   node.right.right.left=Node(9)
   node.right.right.right=Node(11)
   print("Inorder traversal of the tree is:")
   inorder(node)
   print("Finding the inorder sucessor of the node")
   ptr=find_node(node,int(sys.argv[1]))
   try:
     print(inorder_sucessor(node,ptr).value)
   except Exception as e:
     print("No sucessor for this node")


   
  
          
              

