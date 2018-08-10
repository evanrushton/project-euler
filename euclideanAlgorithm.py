import sys

def gcd(n, m):
  if not isinstance( n, ( int, long) ) or not isinstance( m, ( int, long) ):
    print 'Please input two integers for gcd(n, m)'
    sys.exit(1)
  elif n > m: # Make sure m > n
    temp = m
    m = n
    n = temp
  while True:
    r = m % n
    if r == 0:
      return n
    m = n
    n = r

