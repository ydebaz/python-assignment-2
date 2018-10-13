def count_evens(nums):
  q=0
  for i in range(len(nums)):
    if nums[i]%2==0:
      q=q+1
  return q
