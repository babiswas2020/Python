def partition(l):
  temp=0
  track=-1
  pivot=l[len(l)-1]
  for i in range(1,len(l)-1):
     if l[i]<pivot:
         track+=1
         l[track],l[i]=l[i],l[track]
  track+=1
  l[track],l[-1]=l[-1],l[track]
  return track

if __name__=="__main__":
   l=[12,10,9,13,14,8,7,11]
   partition(l)
   print(l)
