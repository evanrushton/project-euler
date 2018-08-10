from primeSieve import *

RANGE = 10 ** 6
def truncateLeft(num):
  n = len(str(num))
  while n > 0:
    print 'left', num
    if not isPrime(num):
      print 'false', num
      return False
    num -= (num / 10 ** (n - 1)) * 10 ** (n - 1)
    n -= 1
  return True

def truncateRight(num):
  n = len(str(num))
  while num > 0:
    print 'right', num
    if not isPrime(num):
      print 'false', num
      return False
    num /= 10 
  return True

primes = primeSieve(RANGE)
truncatablePrimes = []
for prime in primes:
  if truncateLeft(prime) and truncateRight(prime):
    truncatablePrimes.append(prime)
print truncatablePrimes
print sum(truncatablePrimes) - (2 + 3 + 5 + 7)
