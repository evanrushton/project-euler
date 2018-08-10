from primeFactors import *

# Does the num contain n prime factors?
def nPrimes(num, n): 
  factors = set(primeFactors(num))
  return len(factors) == n

notFound = True
i = 1
while notFound:
  i += 1
  if nPrimes(i, 4) and nPrimes(i+1, 4) and nPrimes(i+2, 4) and nPrimes(i+3, 4):
    notFound = False
    print i
#for i in range(20):
#  print 'Does %d contain 2 prime factors?' % (i), nPrimes(i, 2)
