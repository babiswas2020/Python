class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


def min(root):
  while root.left!=None:
       root=root.left
  return root

def max(root):
   while root.right!=None:
        root=root.right
   return root

def find_sucessor(node,x):
    if not node:
       return None
    else: 
         if node.left and node.left==x:
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
    if (x.right!=None):
      ptr=min(x.right)
      return ptr
    else:
       ptr=max(node)
       if ptr==x:
          return None
       elif node==x:
          return None
       else:
          ptr=find_sucessor(node,x)
          return ptr

if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.right=Node(21)
   node.left.left=Node(1)
   node.left.right=Node(9)
   node.left.right.left=Node(8)
   node.left.right.right=Node(10)
   node.right.left=Node(18)
   node.right.right=Node(23)
   node.right.right.left=Node(22)
   print(inorder_sucessor(node,node.left.right.left).value)

   
   


    