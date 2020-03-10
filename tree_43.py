class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def inorder(node):
    if node:
      inorder(node.left)
      print(node.value)
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
         

def common_nodes(root1,root2):
    stack1=[]
    stack2=[]
    while True:
        if root1:
           stack1.append(root1)
           root1=root1.left
        elif root2:
           stack2.append(root2)
           root2=root2.left
        elif stack1 and stack2:
            root1=stack1[-1]
            root2=stack2[-1]
            if root1.value==root2.value:
               print(root1.value)
               root1=stack1.pop()
               root2=stack2.pop()
               root1=root1.right
               root2=root2.right
            elif root1.value>root2.value:
               root2=stack2.pop()
               root2=root2.right
               root1=None
            elif root1.value<root2.value:
               root1=stack1.pop()
               root1=root1.right
               root2=None
        else:
              break

if __name__=="__main__":
   print("Constructing Tree1")
   node=Node(12)
   insert(node,21)
   insert(node,32)
   insert(node,18)
   insert(node,20)
   insert(node,16)
   insert(node,6)
   insert(node,4)
   insert(node,8)
   insert(node,1)
   insert(node,5)
   print("Constructing Tree2")
   node1=Node(12)
   insert(node1,36)
   insert(node1,32)
   insert(node1,21)
   insert(node1,5)
   insert(node1,7)
   insert(node1,8)
   insert(node1,6)
   common_nodes(node,node1)

   
   

 
