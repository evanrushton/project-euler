from primeSieve import *

# List needs to end 10^6 / 22
primes = list(primeSieve(1,10**6 / 22)) 
maxLength = 21
value = 953
# Create long sums of primes less than 10^6 that are prime 
for i in range(len(primes)):
  total = primes[i]
  count = 1
  for j in range(i+1, len(primes)):
    count += 1 
    total += primes[j]
    if total > 10**6:
      break 
    if count > maxLength and isPrime(total):
      maxLength = count
      value = total
print maxLength, value
