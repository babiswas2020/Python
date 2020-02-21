class Node:
   def __init__(self,x,dist):
       self.x=x
       self.dist=dist

def isinside(x,N):
   if x<0 or x>=N:
      return False
   return True


def min_steps(l):
   dx=[1,-1]
   queue=[]
   queue.append(Node(0,0))
   visited=[False]*len(l)
   visited[0]=True
   while queue:
     m=queue.pop(0)
     if m.x==len(l)-1:
        return m.dist
     for i in range(2):
        X=m.x+dx[i]
        if isinside(X,len(l)):
           if not visited[X]:
              queue.append(Node(X,m.dist+1))
     index=[i for i,j in enumerate(l) if j==l[m.x]]
     for k in index:
        if visited[k]==False:
           queue.append(Node(k,m.dist+1))

if __name__=="__main__":
   l=[0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
   print(min_steps(l))
