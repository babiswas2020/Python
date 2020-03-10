class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def isleaf(node):
   if not node:
      return False
   if node.left==None and node.right==None:
      return True
   return False

def postorder(node):
    stack1=[]
    stack1.append(node)
    while stack1:
       temp=stack1.pop()
       while temp and (not isleaf(temp)):
           if temp.left:
              stack1.append(temp.left)
           if temp.right:
              stack1.append(temp.right)
           temp=stack1.pop()
       if temp:
          if isleaf(temp):
             print(temp.value)

if __name__=="__main__":
    node=Node(12)
    node.left=Node(10)
    node.right=Node(21)
    node.left.left=Node(8)
    node.left.right=Node(11)
    node.right.left=Node(18)
    node.right.right=Node(23)
    postorder(node)

       
    