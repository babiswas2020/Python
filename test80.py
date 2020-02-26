import sys
def fib(n):
   if n>=0:
       table[0]=0
       table[1]=1
       for i in range(2,n+1):
          table[i]=table[i-1]+table[i-2]
       return table[n]
   else:
      raise Exception("Exception Occured")

if __name__=="__main__":
   table=[0]*(int(sys.argv[1])+1)
   print(fib(int(sys.argv[1])))


