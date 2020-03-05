class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def height(node):
    if node:
       queue=[]
       queue.append(node)
       count=0
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
    else:
      return 0

def diameter(node):
   right=left=0
   l_height=r_height=0
   if node:
      if node.left:
         left=diameter(node.left)
      if node.right:
         right=diameter(node.right)
      if node.left:
         l_height=height(node.left)
      if node.right:
         r_height=height(node.right)
      return max(max(right,left),l_height+r_height+1)
   else:
      return 0

if __name__=="__main__":
   node=Node(12)
   node.left=Node(15)
   node.left.right=Node(21)
   node.left.left=Node(25)
   node.right=Node(20)
   node.right.left=Node(19)
   node.right.right=Node(26)
   node.right.right.right=Node(30)
   node.right.right.right.right=Node(45)
   node.right.right.right.right.right=Node(62)
   print(diameter(node))
