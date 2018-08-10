import math

input_value = int(input("Enter value for n"))
sieve_max = 5000000
# max_range = int(math.ceil(math.sqrt(input_value)) + 1)
max_range = int(math.ceil(math.sqrt(sieve_max)) + 1)
primes =[]
factors =[]
value = input_value

sieve = [True] * sieve_max # sieve[n] returns true if n is prime

for i in range(2, max_range):
    if sieve[i]:
      primes.append(i)
      for j in range(2, max_range / i + 1):
        sieve[j*i] = False

for p in primes:
    while value % p == 0:
      factors.append(p)
      value = value / p

if value != 1:
  factors.append(value)

print "primes = " + str(primes)
print "factors = " + str(factors)
print "max = " + str(factors[-1])