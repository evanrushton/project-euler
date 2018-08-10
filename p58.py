from primeSieve import *

diagonal = [1]
primes = []
ratio = 0.5
bottomRight = 1
i = 0 
while ratio > 0.1:
  i += 1
  sideLength = 2 * i + 1 # Odd length sides
  for corner in range(1, 5):
    value = bottomRight + corner * (sideLength - 1)
    diagonal.append(value) # Add by 2 three times
    if isPrime(value):
      primes.append(value)
  if len(primes):
    ratio = float(len(primes))/len(diagonal)
  bottomRight += 4*sideLength - 4 # Next bottom right 
print sideLength
