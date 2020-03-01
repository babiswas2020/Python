def rearrange(l):
    track=-1
    for i in range(len(l)):
       if l[i]<0:
          track+=1
          l[track],l[i]=l[i],l[track]
    pos,neg=track+1,0
    while(pos<len(l) and neg<pos and l[neg]<0):
         l[neg],l[pos]=l[pos],l[neg]
         pos=pos+1
         neg=neg+2

if __name__=="__main__":
   l=[-1, 2, -3, 4, 5, 6, -7, 8, 9] 
   rearrange(l)
   print(l)
   m=[1,3,4,-2,-5,-7,6,8,9,10,-11,-12,-14,-2,1,1]
   rearrange(m)
   print(m)

      
    