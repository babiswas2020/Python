l=[[1,2,3],[1,0,1],[1,1,3],[1,4,5],[0,3,1]]

def get_key(m):
   return m[1]
if __name__=="__main__":
  print(sorted(l,key=get_key))
