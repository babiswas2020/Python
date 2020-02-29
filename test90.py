import copy
def rearrangement(l):
   l=sorted(l)
   m=copy.deepcopy(l)
   mid=len(l)//2
   mid1=copy.deepcopy(mid)
   mid1=mid1+1
   for i in range(0,len(l),2):
      if mid>=0:
        l[i]=m[mid]
        mid=mid-1
   for i in range(1,len(l),2):
      if mid1<len(l):
         l[i]=m[mid1]
         mid1=mid1+1
   return l

if __name__=="__main__":
   l=[1, 2, 3, 4, 5, 6, 7]
   print(rearrangement(l))

         
         
       
 