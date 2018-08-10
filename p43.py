from primeSieve import *
import itertools
digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# create ordered list of 10-digit pandigitals
# 9 + permutations of 87654321 and first that isPrime is solution
def pandigitize(nums):
  pans = []
  perms = itertools.permutations(nums)
  for p in perms:
    pan = 0 
    for idx, val in enumerate(p):
      pan += val * (10 ** ((len(nums)-1) - idx))
    pans.append(pan)
  return pans 

def substringDivisible(s):
  primes = primeSieve(18) 
  for i in xrange(2, 9):
    print i, s[i-1:i+2], primes[i-2]
    if int(s[i-1:i+2]) % primes[i-2] != 0:
      # print 'Failed'
      return False
  print 'SUCCESS - ', s
  return True

ssd = [] # substringdivisible
list = pandigitize(digits)
for pan in list:
  # print 'Next Pan = ', pan
  if substringDivisible(str(pan)):
    ssd.append(pan)
print sum(ssd)
