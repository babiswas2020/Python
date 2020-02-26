import sys

def fib(n,table):
   if n>=0:
      if table[n]==0:
         if n<=1:
           table[n]=n
         else:
           table[n]=fib(n-2,table)+fib(n-1,table)
         return table[n]
      else:
         return table[n]
   else:
      raise Exception("Negative no not allowed")

if __name__=="__main__":
   n=int(sys.argv[1])
   table=[0]*(n+1)
   print(fib(n,table))


