from primeSieve import *
import sys
from collections import defaultdict

######## INITIALIZE VARS ########
NUM = 15000
primes = primeSieve(3, NUM)
concatDict = defaultdict(lambda : None) # dict of {prime_index: concat_set} pairs
# endPrimes = len(primes) - 1
# primeStart = 0

######## HELPER FUNCTIONS ########
def concatSet(p1):
  """Returns a set of primes whose concatinations
  with the prime at this index are also prime"""
  pairs = set()
  for p2 in range(p1 + 1, len(primes)-1):
    if isPrimeConcat(primes[p1], primes[p2]):
      pairs.add(primes[p2])
  return pairs 
    
def isPrimeConcat(prime_1, prime_2):
  """Returns a bool indicating if both concatinations of the prime inputs are
  also prime"""
  s_1 = str(prime_1)
  s_2 = str(prime_2)
  return isPrime(int(s_1 + s_2)) and isPrime(int(s_2 + s_1))

def checkPrimePairSet():
  """Prints 5 primes that create a prime pair set"""
  result = sys.maxint
  for a in range(len(primes)):
    if primes[a] * 5 >= result: break
    if concatDict[a] is None: concatDict[a] = concatSet(a)

    for b in range(a + 1, len(primes)):
      if primes[a] + primes[b] * 4 >= result: break
      if not primes[b] in concatDict[a]: continue
      if concatDict[b] is None: concatDict[b] = concatSet(b)

      for c in range(b + 1, len(primes)):
        if primes[a] + primes[b] + primes[c] * 3 >= result: break
        if not primes[c] in concatDict[a] or not primes[c] in concatDict[b]: continue
        if concatDict[c] is None: concatDict[c] = concatSet(c)

        for d in range(c + 1, len(primes)):
          if primes[a] + primes[b] + primes[c] + primes[d] * 2 >= result: break
          if not primes[d] in concatDict[a] or not primes[d] in concatDict[b] or not primes[d] in concatDict[c]: continue
          if concatDict[d] is None: concatDict[d] = concatSet(d)

          for e in range(d + 1, len(primes)):
            if primes[a] + primes[b] + primes[c] + primes[d]  + primes[e] >= result: break
            if not primes[e] in concatDict[a] or not primes[e] in concatDict[b] or not primes[e] in concatDict[c] or not primes[e] in concatDict[d]: continue
            if result > primes[a] + primes[b] + primes[c] + primes[d]  + primes[e]:
              result =  primes[a] + primes[b] + primes[c] + primes[d]  + primes[e]
              print primes[a], primes[b], primes[c], primes[d], primes[e], result
    print 'Lowest sum of 6 primes ', result

######## MAIN ########
checkPrimePairSet()

