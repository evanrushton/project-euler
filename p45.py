import gmpy2

def isTriangle(n):
  return (gmpy2.sqrt(8 * n + 1) + 1) / 2.0 == int((gmpy2.sqrt(8 * n + 1) + 1) / 2.0)

def isPentagon(n):
  return (gmpy2.sqrt(24*n + 1) + 1) / 6.0 == int((gmpy2.sqrt(24*n + 1) + 1) / 6.0)

def isHexagon(n):
  return (gmpy2.sqrt(8*n + 1) + 1) / 4.0 == int((gmpy2.sqrt(8*n + 1) + 1) / 4.0)

i = (gmpy2.sqrt(24*40755 + 1) + 1) / 6.0 
while True:
  i +=1
  n = i * (3*i - 1) / 2
  if isHexagon(n):
    print n
    break
