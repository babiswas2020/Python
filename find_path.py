from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def find_path(self,u,v):
       prev=self.shortest_path(u,v)
       path=[]
       i=v
       while  i!=None:
          path.append(i)
          i=prev[i]
       path[:]=path[::-1]
       if path[0]==u:
          print(f"There is a path from u to v {path}")
       else:
          printf(f"There is no path from u to v")

   def shortest_path(self,u,v):
       visited=[False]*self.vertex
       queue=[]
       prev=[None]*self.vertex
       queue.append(u)
       visited[u]=True
       while queue:
           m=queue.pop(0)
           for i in self.graph[m]:
              if not visited[i]:
                 queue.append(i)
                 visited[i]=True
                 prev[i]=m
       return prev

if __name__=="__main__":
   graph=Graph(8)
   graph.add_edges(2,1)
   graph.add_edges(1,0)
   graph.add_edges(0,3)
   graph.add_edges(3,7)
   graph.add_edges(3,4)
   graph.add_edges(7,4)
   graph.add_edges(7,6)
   graph.add_edges(6,5)
   graph.add_edges(4,5)
   graph.add_edges(4,6)
   graph.find_path(0,7)

   