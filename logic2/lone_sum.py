def lone_sum(a, b, c):
  y=a+b+c
  if a==b and b==c and a==c:
    return 0
  else  :
   if a==b:
    y=y-b-a
   elif b==c:
    y=y-c-b
   elif a==c:
    y=y-c-a
  
  return y  
