from primeSieve import *
import gmpy2

# Return generator of squared numbers
def listSquares(lim):
  for i in xrange(lim+1):
    yield i **2

i = 2
while True:
  i += 1
  odd = 2*i + 1
  hasSum = False
  notPrime = not isPrime(odd)
  if notPrime:
    for prime in primeSieve(odd-1):
      limit = int(gmpy2.sqrt((odd - prime)/2))
      for square in listSquares(limit):
        if odd == prime + 2*square:
          hasSum = True
          break
      if hasSum:
        break
  if notPrime and not hasSum:
    print 'Smallest odd composite not sum of prime and twice square ', odd
    break
