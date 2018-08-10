from primeSieve import *

primes = list(primeSieve(9999))[168:] # 4-digit primes
indeces = len(primes)
solutions = [] 
for idx in range(indeces):
  for nxt in range(idx + 1, indeces):
    diff = primes[nxt] - primes[idx]
    if primes[nxt] + diff in primes:
      first = str(primes[idx])
      second = str(primes[nxt])
      third = str(primes[nxt] + diff)
      if sorted(first) == sorted(second) and sorted(second) == sorted(third):
        solutions.append(first + second + third)
print solutions
