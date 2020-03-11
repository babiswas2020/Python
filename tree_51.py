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


def is_leaf(node):
    if not node:
       return False
    if node.left==None and node.right==None:
        return True
    return False
    

def leaf_node(node):
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
   node=Node(12)
   insert(node,21)
   insert(node,15)
   insert(node,11)
   insert(node,4)
   insert(node,10)
   insert(node,1)
   insert(node,5)
   insert(node,3)
   inorder(node)
   print("Printing leaf nodes")
   leaf_node(node)



   
    