def partition(l,start,end):

    wall=start-1

    pivot=l[end]

    for i in range(start,end):

        if l[i]<pivot:

          wall=wall+1

          l[wall],l[i]=l[i],l[wall]

    wall=wall+1

    l[wall],l[end]=pivot,l[wall]

    return wall



def Quick_sort(l,start,end):

    if start<end:

       index=partition(l,start,end)

       Quick_sort(l,start,index-1)

       Quick_sort(l,index+1,end)



l=[12,11,10,9,14,15,8,6]

Quick_sort(l,0,7)

print(l)