import queue

class Node:
   def __init__(self,x,dist):
       self.x=x
       self.dist=dist


def min_operation(x,y):
    que=queue.Queue()
    s=set()
    node=Node(x,0)
    que.put(node)
    while que:
        m=que.get()
        if m.x==y:
           return m.dist
        X=m.x*2
        Y=m.x-1
        if X==y or Y==y:
           return m.dist+1
        if X not in s:
           que.put(Node(X,m.dist+1))
        if Y not in s and Y>=0:
           que.put(Node(Y,m.dist+1))

if __name__=="__main__":
   print(min_operation(4,7))