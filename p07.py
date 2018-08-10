import math

sieve_max1 = 10000000
max_range1 = int(math.ceil(math.sqrt(sieve_max1)) + 1)
sieve_max2 = 3000000000
max_range2 = int(math.ceil(math.sqrt(sieve_max2)) + 1)
sieve_max3 = 30000000000
max_range3 = int(math.ceil(math.sqrt(sieve_max3)) + 1)
primes =[]

sieve = [True] * sieve_max2 # sieve[n] returns true if n is prime

for i in xrange(2, max_range1):
    if sieve[i]:
      primes.append(i)
      for j in range(2, max_range3 / i + 1):
        sieve[j*i] = False

for i in xrange(max_range1, max_range2):
  if sieve[i]:
    primes.append(i)
    for j in range(2, max_range3 / i + 1):
      sieve[j*i] = False

for i in xrange(max_range2, max_range3):
  if len(primes) == 10001:
    break
  if sieve[i]:
    primes.append(i)
    for j in range(2, max_range3 / i + 1):
      sieve[j*i] = False

print "primes = " + str(primes)
print "lengthPrimes" + str(len(primes))
