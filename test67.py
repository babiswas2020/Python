def partition(l):
    temp=0
    track=-1
    pivot=l[len(l)-1]
    for i in range(1,len(l)-1):
       if l[i]<pivot:
         track=track+1
         temp=l[track]
         l[track]=l[i]
         l[i]=temp
    track=track+1
    temp=l[track]
    l[track]=pivot
    l[len(l)-1]=temp
    return track


def qsort(l,start,end):
    if start<end:
       pos=partition(l)
       qsort(l[start:pos-1],start,pos-1)
       qsort(l[pos+1:],pos+1,end)



if __name__=="__main__":
   l=[12,11,10,9,13,14,15,11]
   qsort(l,0,len(l))
   print(l)


    