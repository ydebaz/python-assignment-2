def make_bricks(small, big, goal):
  if goal%5<=small and (goal-small)<=big*5:
   return True
  else :
   return False
