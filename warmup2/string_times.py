def string_times(str, n):
  if n==0:
    return ""
  else:
   i=1
   str2=str
   while i< n:
     str2=str2+str
     i=i+1
   return str2  
