from fractions import Fraction

def updateFraction(frac):
  return Fraction(1/(2 + frac))

result = 0
repeatFrac = 0
for i in xrange(0,1001):
  repeatFrac = Fraction(updateFraction(repeatFrac))
  frac = Fraction(1 + repeatFrac)
  print i, frac.numerator
  print i, frac.denominator
  num = len(str(frac.numerator))
  den = len(str(frac.denominator))
  if num > den:
    result += 1
    print i, num, den 
print result # number of times there are more digits in the numerator guess = 1500



