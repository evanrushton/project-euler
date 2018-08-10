from primeSieve import *

'''Want to avoid checking pairs TWICE
Create sets of goodPrimes, goodSets, Set(p1, p2, p3)
'''

primes = primeSieve(3, 10**4)
endPrimes = len(primes) - 1
primeStart = 0

# IN two primes  OUT bool
# Check that both concatinations are prime, return result
def isConcatPrime(prime_1, prime_2):
  s_1 = str(prime_1)
  s_2 = str(prime_2)
  return isPrime(int(s_1 + s_2)) and isPrime(int(s_2 + s_1))

# Return list with all pairs of primes that concatenate to make primes
def buildGoodPairsSet():
  goodPairs = set() 
  for p1_idx, prime_1 in enumerate(primes):
    for p2_idx in range(p1_idx + 1, endPrimes):
      prime_2 = primes[p2_idx]
      # print prime_1, prime_2
      if isConcatPrime(prime_1, prime_2):
        goodPairs.add(frozenset([prime_1, prime_2]))
  return goodPairs

def buildGoodNSet(setN):
  goodN = set()
  for idx, set_1 in enumerate(setN):
    for idx_2 in range(idx + 1, len(setN) - 1):
      set_2 = setN[idx_2]
      diff = set_1 ^ set_2
      print '\nset_1', idx, set_1, '\nset_2', idx_2, set_2, '\ndiff', diff, '\nlen', len(diff)
      # If symmetric difference is a good pair then the union is a goodSet
      if len(diff) == 2 and diff in goodPairs and diff not in goodN:
        goodN.add(set_1 | set_2)
        # print goodN
  return goodN


goodPairs = buildGoodPairsSet()
goodTrips = buildGoodNSet(list(goodPairs))
# print goodTrips
goodQuads = buildGoodNSet(list(goodTrips))
# print goodQuads
goodPents = buildGoodNSet(list(goodQuads))
print goodPents
# for prime_1, p1_idx in enumerate(primes):

