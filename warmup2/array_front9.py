def array_front9(nums):
  for i in range(0,len(nums)):
    if i>3:
      return False   
    elif nums[i]==9:
     return True
  return False   
