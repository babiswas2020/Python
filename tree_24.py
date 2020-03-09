class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


def find_node(root,x):
    if not root:
       return None
    elif root.vlaue==x:
       return root
    else:
      temp1=find_node(root.left,x) 
      temp2=find_node(root.right,x)
      if temp1:
         return temp1
      elif temp2:
         return temp2
      else:
         return None

def find_parent(root,node):
    if root.left==node or root.right==node:
             return node
    else:
      temp1=find_parent(root.left,node)
      temp2=find_parent(root.right,node)
      if temp1:
         return temp1
      elif temp2:
         return temp2
      else:
         return

def find_parent_node(root,x):
    if root==None:
       return None
    else:
       node1=find_node(root,x)
       parent=find_parent(root,node1)
       return parent

def inorder(node):
    if node:
       if node.left:
          inorder(node.left)
       print(node.value)
       if node.right:
          inorder(node.right)

if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.left.left=Node(1)
   node.left.right=Node(9)
   node.left.right.right=Node(10)
   node.left.right.left=Node(8)
   node.right=Node(21)
   node.right.left=Node(18)
   node.right.right=Node(23)
   node.right.right.left=Node(22)
   temp=node.left.right
   print("Printing inorder traversal")
   inorder(node)
   parent=find_parent_node(node,9)
   print(parent.value)


