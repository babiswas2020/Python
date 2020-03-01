def partition(l,start,end):
    wall=start-1
    pivot=l[end]
    for i in range(start+1,end-1):
       if l[i]<pivot:
         wall+=1
         l[wall],l[i]=l[i],l[wall]
    wall+=1
    l[wall],l[end]=pivot,l[wall]
    return wall

def Qsort(l,start,end):
   if start<end:
      pos=partition(l,start,end)
      Qsort(l,start,pos-1)
      Qsort(l,pos+1,end)

if __name__=="__main__":
   l=[12,11,10,9,14,15,8,6]
   Qsort(l,0,7)
   print(l)

        