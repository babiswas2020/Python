class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def height(node):
    temp=node
    count=0
    queue=[]
    queue.append(temp)
    while queue:
        queue_len=len(queue)
        if queue_len:
           count=count+1
        while queue_len:
           m=queue.pop(0)
           if m.left:
              queue.append(m.left)
           if m.right:
              queue.append(m.right)
           queue_len=queue_len-1
    return count

def is_present(node,value):
   if node==None:
      return False
   elif node.value==value:
      return True
   else:
      return is_present(node.left,value) or is_present(node.right,value)

def lca_driver(node,val1,val2):
    if node:
       if node.value==val1 or node.value==val2:
          return node
       else:
           left=lca_driver(node.left,val1,val2)
           right=lca_driver(node.right,val1,val2)
           if left and right:
               return node
           elif left==None:
               return right
           elif right==None:
               return left
    else:
        return None


def lca(node,val1,val2):
    if node==None:
       return None
    elif is_present(node,val1) and is_present(node,val2):
         return lca_driver(node,val1,val2)
    else:
         return None

if __name__=="__main__":
   node=Node(12)
   node.left=Node(14)
   node.left.right=Node(17)
   node.left.left=Node(18)
   node.right=Node(11)
   node.right.left=Node(34)
   node.right.right=Node(28)
   node.right.right.left=Node(16)
   node.right.right.right=Node(50)
   print(height(node))
   print(is_present(node,28))
   print(is_present(node,24))
   print(lca(node,34,50).value)



   


            
        