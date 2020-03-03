class Cell:
   def __init__(self,x,y,dist):
       self.x=x
       self.y=y
       self.dest=dist


def is_inside(x,y,N,M):
    if x<0 or x>=N:
        return False
    if y<0 or y>=N:
        return False
    if M[x][y]=='#':
        return False
    return True

def find_path(tpos,pos,M,N):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited=[[0 for i in range(N)] for i in range(N)]
    queue=[]
    queue.append(Cell(pos[0],pos[1],0))
    visited[pos[0]][pos[1]]=1
    while queue:
        m=queue.pop(0)
        if m.x==tpos[0] and m.y==tpos[1]:
            return m.dest
        for i in range(4):
          X=m.x+dx[i]
          Y=m.y+dy[i]
          if is_inside(X,Y,N,M):
             if visited[X][Y]==False:
                queue.append(Cell(X,Y,m.dest+1))
                visited[X][Y]=True

if __name__=="__main__":
  N=4
  M=[[3,3,1,'#'],[3,'#',3,3],['E',3,'#',3],['#',3,3,3]]
  pos=[0,2]
  tpos=[2,0]
  print(find_path(tpos,pos,M,N))
             