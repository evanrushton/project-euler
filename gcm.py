from primeSieve import *

### Perform prime factorization of an integer 
#   INPUT: Integer value
#   OUTPUT: List of factors as tuples (prime, power)
def primeFactors(num):
  primes_powers = []
  for prime in primeSieve(2, num):
    power = 0
    while num % prime == 0:
      num /= prime
      power += 1
    if power > 0:
      primes_powers.append((prime, power))
    if num == 1:
      break
    if not primes_powers:
      primes_powers.append((num, 1))
  return primes_powers


### Find the least common multiple for two integers
#   INPUT: 2 integer values
#   OUTPUT: LCM of those integers 
def LCM(a, b):
  primes_powers_a = primeFactors(a)
  primes_powers_b = primeFactors(b)
  multiple = 1
  dict_primes = {} 
  for prime_power_a in primes_powers_a:
    prime_a = prime_power_a[0]
    power_a = prime_power_a[1] 
    dict_primes[prime_a] = power_a     # Add prime:power for a to dict
  for prime_power_b in primes_powers_b:
    prime = prime_power_b[0] 
    power_b = prime_power_b[1]
    power_a = dict_primes.get(prime)
    power = max(power_b,power_a)       # Update power for primes in a and b
    dict_primes[prime] = power         # Add prime:power for b to dict
    for prime, power in dict_primes.iteritems():
      multiple *= (prime ** power)
  return multiple


first = int(raw_input("Enter first digit "))
second = int(raw_input("Enter second digit "))
print LCM(first, second)

