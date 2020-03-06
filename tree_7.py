class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def insert(self,value):
       if self.value>value:
           if self.left:
              self.left.insert(value)
           else:
              self.left=Node(value)
       elif self.value<value:
           if self.right:
              self.right.insert(value)
           else:
              self.right=Node(value)
       else:
         print("Duplication not allowed")

   def height(self):
       count=0
       queue=[]
       queue.append(self)
       while queue:
          que_len=len(queue)
          if que_len:
             count=count+1
          while que_len:
             m=queue.pop(0)
             if m.left:
                queue.append(m.left)
             if m.right:
                queue.append(m.right)
             que_len=que_len-1
          
       return count

if __name__=="__main__":
   node=Node(12)
   node.insert(21)
   node.insert(18)
   node.insert(24)
   node.insert(5)
   node.insert(9)
   node.insert(7)
   print(node.height())



             
      
