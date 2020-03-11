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

def print_path(node,stack):
    if not node:
       return 
    stack.append(node)
    if node.left:
       print_path(node.left,stack)
    print([i.value for i in stack])
    if node.right:
       print_path(node.right,stack)
    stack.pop()

def is_leaf(node):
  if node==None:
     return False
  if node.left==None and node.right==None:
     return True
  return False

def print_leaf(node):
    temp=None
    stack=[]
    stack.append(node)
    while stack:
       temp=stack.pop()
       while temp and (not is_leaf(temp)):
           if temp.right:
               stack.append(temp.right)
           if temp.left:
               stack.append(temp.left)
           temp=stack.pop()
       if temp:
          if is_leaf(temp):
             print(temp.value)
             
if __name__=="__main__":
   stack=[]
   node=Node(12)
   node.left=Node(21)
   node.right=Node(18)
   node.left.right=Node(25)
   node.left.left=Node(20)
   node.right.left=Node(15)
   node.right.right=Node(23)
   inorder(node)
   print("Print all the path of the tree")
   print_path(node,stack)
   print("Printing the leaf nodes")
   print_leaf(node)

  
