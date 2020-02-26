import sys
def fib(n):
  if n>=0:
     if n<=1:
       return n
     return fib(n-1)+fib(n-2)
  else:
     raise Exception("Number is negative number")

if __name__=="__main__":
   print(fib(int(sys.argv[1])))



