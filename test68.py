from contextlib import contextmanager

@contextmanager
def fun(name):
  try:
     m=open(name,'w')
     yield m
  finally:
     m.close()

if __name__=="__main__":
   with fun("test1.txt") as f:
       f.write("Hello")
       f.write("Bello")


     