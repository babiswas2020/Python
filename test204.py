class A:
   def __init__(self,name):
       self.name=name
   def __enter__(self):
       self.m=open(self.name,'w')
       return self.m
   def __exit__(self,exc_x,exc_y,exc_z):
       if self.m:
          self.m.close()
if __name__=="__main__":
   with A('file1.txt') as a:
       a.write("Hello")
       a.write("Bello")
       a.write("Mello")
