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

def find_max_util(node):
   res1=res2=0
   if node==None:
      return -1
   else:
      res=node.value
      if node.left:
        res1=find_max_util(node.left)
      if node.right:
        res2=find_max_util(node.right)
      if res<res2:
         res=res2
      if res<res1:
         res=res1
      return res



if __name__=="__main__":
   node=Node(12)
   node.right=Node(21)
   node.left=Node(6)
   node.right.left=Node(18)
   node.right.right=Node(24)
   node.right.left.left=Node(16)
   node.right.left.right=Node(20)
   node.left.right=Node(10)
   node.left.left=Node(4)
   inorder(node)
   print("Printing maximum value of tree")
   print(find_max_util(node))

