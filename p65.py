from fractions import Fraction
NUM_CONVERGENTS = 100

def getDivisorList(k):
  list = []
  for i in range(1, k + 1):
    list += [1, 2 * i, 1]
  return list

def updateFraction(i, level, divisorList):
  if level == -1:
    return 0
  if level == i:
#    print 'i %s, level %s, 1 / %s' % (i, level, divisorList[i])
    return Fraction( 1 , divisorList[i] )
  else:
#    print 'i %s, level %s, 1 / (%s + )' % (i, level, divisorList[i])
    return Fraction( 1 , (divisorList[i] + updateFraction(i + 1, level, divisorList)) )

def getConvergentList(seed, divisorList, n):
  list = []
  repeatFrac = 0 
  for i in range(n):
    repeatFrac = updateFraction(0, i - 1, divisorList)
    frac = Fraction(seed + repeatFrac)
#    print 'convergent %s, frac = %s +  %s' % (i, seed, repeatFrac)
    list.append(frac)
  return list

convergentList = getConvergentList(2, getDivisorList(NUM_CONVERGENTS), NUM_CONVERGENTS)
num = str(convergentList[99].numerator)
count = 0
for i in range(len(num)):
  count += int(num[i])
print count
