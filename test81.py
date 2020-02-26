def longest_palindrome_substring(str1):
   maxm=0
   if len(str1)>2:
     table=[[0 for i in range(len(str1))] for i in range(len(str1))]
     for i in range(len(str1)):
        table[i][i]=1
        maxm=1
     for i in range(len(str1)):
        if i+1<len(str1) and str1[i]==str1[i+1]:
             table[i][i+1]=1
             maxm=2
     for i in range(len(str1)):
       for j in range(3,len(str1)+1):
          if i+j-1<len(str1):
            if str1[i]==str1[i+j-1]:
               if table[i+1][i+j-2]==1:
                  table[i][i+j-1]=1 
                  if maxm<j:
                     maxm=j       
   elif len(str1)==2:
       if str1[0]==str1[1]:
          return True
       else:
          return False
   elif len(str1)==1:
        return True
   return maxm

if __name__=="__main__":
   print(longest_palindrome_substring("abbdbbdddbbdsdsdddeeeeddweeeeffgdeefffreeeefffffdd"))

   

       