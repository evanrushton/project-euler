import math
digitFactorials = []
for i in xrange(3, 9999999):
  digits = str(i)
  ct = 0
  for ch in digits:
    ct += math.factorial(int(ch))
  if ct == i:
    digitFactorials.append(i)
print digitFactorials
