from primeSieve import *
import itertools
digits = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# create ordered list of 9-digit pandigitals
# 9 + permutations of 87654321 and first that isPrime is solution
def pandigitize(nums):
  pans = []
  start = nums[0]
  end = nums[1:len(nums)]
  perms = itertools.permutations(end)
  for p in perms:
    pan = start * (10 ** (len(nums)-1))
    for idx, val in enumerate(p):
      pan += val * (10 ** ((len(nums)-2) - idx))
    pans.append(pan)
  return pans 

primeFound = False
for n in range(len(digits)):
  if primeFound:
    break
  vals = digits[n:]
  list = pandigitize(vals)
  for n in list:
    print n
    if isPrime(n):
      print 'found prime ', n
      primeFound = True
      break
