class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

def is_leaf(node):
   if node:
      return (node.left==None) and (node.right==None)
   return False

def find_first_leaf(node1,node2):
    temp1=temp2=None
    stack1=[]
    stack2=[]
    stack1.append(node1)
    stack2.append(node2)
    while stack1 or stack2:
       if len(stack1)==0 or len(stack2)==0:
          return
       temp1=stack1.pop()
       while temp1 and (not is_leaf(temp1)):
           if temp1.right:
              stack1.append(temp1.right)
           if temp1.left:
              stack1.append(temp1.left)
           temp1=stack1.pop()
       temp2=stack2.pop()
       while temp2 and (not is_leaf(temp2)):
           if temp2.right:
              stack2.append(temp2.right)
           if temp2.left:
              stack2.append(temp2.left)
           temp2=stack2.pop()

       if temp1 and temp2:
         if temp1.value!=temp2.value:
            print(f"{temp1.value}!={temp2.value}")
            return

if __name__=="__main__":
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
   find_first_leaf(node,node1)
   





           
              
           
      
       
      
        