import math

# Check if a value is prime
def isPrime(num):
  if num < 2:
    return False

  for i in xrange(2, int(num**0.5) + 1):
    if num % i ==0:
      return False
  return True

# Return generator or list of prime numbers
def primeSieve(start, sieveSize):
  sieve = [True] * sieveSize
  if sieveSize >= 1: sieve[0] = False
  if sieveSize > 1: sieve[1] = False

  for i in xrange(2, int(sieveSize**0.5) + 1):
   pointer = i * 2
   while pointer < sieveSize:
     sieve[pointer] = False
     pointer += i

  primes = []
  for i in range(start, sieveSize):
    if sieve[i]:
      primes.append(i)
#      yield i          # return generator
  return primes        # return list

