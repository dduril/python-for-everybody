def chop(t):
  s = t[1:len(t)-1]
  return s

nums = [1, 2, 3, 4, 5, 6, 7, 8]
for n in nums:
  print n
  
print chop(nums)