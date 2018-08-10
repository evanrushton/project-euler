# Totient Maximum
# Goal: Maximize n / phi(n) for n <= 10^6
# from primeFactors import *
from primeSieve import *

# Collect user input, must be an integer
def getMaxMin():
  while True:
    try:
      min = int(raw_input("Input a minimum number to limit search. "))
    except ValueError:
      print "min must be an integer"
    try:
      max = int(raw_input("Input a maximum number to limit search. "))
    except ValueError:
      print "min must be an integer"
    return min, max

# Input: int n
# Output: int count of the number of primes relatively prime to n
def phi(n, rate):
  factors = factorSet(2, set(), n) 
  count = 0
  # print factors
  for i in xrange(1, n):
    if any(i % factor == 0 for factor in factors):
      # print i, ' not relatively prime'
      continue 
    # print i, 'relatively prime with ', n
    count += 1
    if n / count < rate: # rate becomes smaller than max rate, skip
      return n # break loop, return rate = 1 (always less than max)
  return count

# Find maximum n / phi(n) for n <= 10^6
def maxNtoPhiRatio(min, max):
  valRate = [2, 1]
  for n in xrange(min, max):
    rate = n / phi(n, valRate[1])
    if (rate > valRate[1]):
      valRate = [n, rate]
      print valRate
  return valRate 

### MAIN ###
# min, max = getMaxMin()
# result = maxNtoPhiRatio(min, max)
# print result[0], ' has ratio ', result[1]   
val = 1
primes = primeSieve(2, 10**3)
for prime in primes:
  # print prime, val
  val *= prime
  if val > 10**6:
    val /= prime
    print val
    break
  
  # multiply by consecutive primes until the next value is over 10^6

# Tests
#print phi(n), ' relatively prime integers'

