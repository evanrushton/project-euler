import math
import itertools
indices = range(10)
pos = 10**6 - 1
value = 0
permutations = itertools.permutations(indices)
while indices:
  n = len(indices) - 1
  index = pos / math.factorial(n)
  value += indices.pop(index) * 10**n
  pos -= index * math.factorial(n) 
print list(permutations)[10**6 - 1]
print value
