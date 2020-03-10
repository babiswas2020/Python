class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None
  
def inorder(node,stack):
    if node:
       if node.left:
          inorder(node.left,stack)
       if node.left==None and node.right==None:
          stack.append(node)
       if node.right:
          inorder(node.right,stack)

if __name__=="__main__":
   stack1=[]
   stack2=[]
   print("Constructing Tree1")
   node=Node(5)
   node.left=Node(2)
   node.right=Node(7)
   node.left.left=Node(10)
   node.left.right=Node(11)
   print("Constructing Tree2")
   node1=Node(6)
   node1.left=Node(10)
   node1.right=Node(15)
   print("Performing Inorder of tree 1")
   inorder(node,stack1)
   inorder(node1,stack2)
   A=[i.value for i in stack1]
   B=[j.value for j in stack2]
   for j in B:
     if j not in A:
        print(j)
        break

   
