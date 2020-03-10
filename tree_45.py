class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

def preorder(node):
    stack=[]
    stack.append(node)
    while stack:
       m=stack.pop()
       print(m.value)
       if m.right:
         stack.append(m.right)
       if m.left:
         stack.append(m.left)

if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.left.left=Node(4)
   node.left.right=Node(8)
   node.right=Node(21)
   node.right.left=Node(18)
   node.right.right=Node(25)
   preorder(node)

