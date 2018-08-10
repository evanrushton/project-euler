import itertools as it
import math

def combinations(n, r):
  return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))


# TESTS
nCr = 0
count = 0
for n in xrange(1,101):
  for r in xrange(2,n-1):
    nCr = combinations(n, r)
    if nCr > 10 ** 6:
      count += 1
      print "{}, {}".format(n, r), combinations(n, r)
print count
