class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"

def get_key(obj):
    return obj.a

if __name__=="__main__":
   l=[A(1,2),A(0,2),A(5,3),A(2,4)]
   m=sorted(l,key=get_key)
   for i in m:
      print(i)


   