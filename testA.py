l=[[1,2],[3,4],[5,0],[2,1]]

def get_key(m):
   return m[1]

if __name__=="__main__":
   print(sorted(l,key=get_key))