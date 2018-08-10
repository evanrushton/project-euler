import math
from primeSieve import primeSieve
  

inp = input("Enter target max int")
primes = primeSieve(inp)
print sum(primes)

