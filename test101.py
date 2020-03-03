class Cell:
   def __init__(self,x,y,dist):
      self.x=x
      self.y=y
      self.dist=dist


def is_inside(x,y,N):
    if x<0 or x>=N:
        return False
    if y<0 or y>=N:
        return False
    return True

def find_path(pos,tpos,N):
    dx=[2,2,-2,-2,1,-1,1,-1]
    dy=[1,-1,1,-1,2,2,-2,-2]
    visited=[[0 for i in range(8)] for i in range(8)]
    queue=[]
    visited[pos[0]][pos[1]]=True
    queue.append(Cell(pos[0],pos[1],0))
    while queue:
        m=queue.pop(0)
        if m.x==tpos[0] and m.y==tpos[1]:
           return m.dist
        for i in range(8):
           X=m.x+dx[i]
           Y=m.y+dy[i]
           if is_inside(X,Y,N):
              if not visited[X][Y]:
                 queue.append(Cell(X,Y,m.dist+1))
                 visited[X][Y]=True

if __name__=="__main__":
   print(find_path([0,2],[4,3],5))
  
   