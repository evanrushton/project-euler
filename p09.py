import math

### a < b < c , a + b + c = 1000, a^2 + b^2 = c^2
for a in xrange(1, 333):
  for b in xrange(a, 499):
    c = 1000 - (a + b)
    if a*a + b*b == c*c:
      print a, b, c, a*b*c
      print a*a, b*b, c*c
