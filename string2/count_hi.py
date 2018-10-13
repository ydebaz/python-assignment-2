def count_hi(str):
  q=0
  for i in range (len(str)-1):
   if str[i]=='h' and str[i+1]=='i':
     q=q+1
  return q   
