from primeSieve import * 
import itertools as it

def isCircular(p):
  # nums = [''.join(item) for item in it.permutations(str(p))]
  nums = []
  next = p
  n = len(str(p))
  for i in range(n):
    next = next % 10 * 10 ** (n - 1) + next / 10
    nums.append(next)
  print nums
  for num in nums:
    if not isPrime(int(num)):
      print "Fail", p, num 
      return False
  return True

sieve = primeSieve(10 ** 6)
circular = []
for prime in sieve:
  if isCircular(prime):
    circular.append(prime)
    print 'WIN', prime
print circular
print len(circular)
