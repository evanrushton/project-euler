import time
import math

def isLychrel(num):
  iter = 0
  tmp = num
  while iter < 50:
    tmp = reverseAndAdd(tmp)
    st = str(tmp)
    if isPalindrome2(st): # Make a numerical isPalindrome()
      return False
    iter += 1
  return True

def reverseAndAdd(num):
  rev = 0
  tmp = num
  while tmp / 10:
    rev += (tmp % 10)
    rev *= 10
    tmp /= 10
  rev += tmp
  return num + rev

def isPalindrome1(st):
  length = len(st)
  for k in range(0, int(math.floor(length / 2))):
      if st[k] != st[length - 1 - k]:
        return False 
  return True

def isPalindrome2(st): # Marginally faster
  l = len(st)
  if l % 2 == 0 and st[:l/2] == st[l/2:][::-1]:
    return True
  elif l % 2 == 1 and st[:l/2] == st[l/2 + 1:][::-1]:
    return True
  return False


### TESTS ###
def timeFunc(fun, st):
  elapsed = 0
  start = time.time()
  test = fun(st)
  stop = time.time()
  diff =  stop - start
  return [test, diff]

RANGE = 10000
# elapsed1 = 0
# elapsed2 = 0
lychrels = []
count = 0
for i in xrange(RANGE):
  if isLychrel(i):
    count += 1
    lychrels.append(i)
print lychrels, count
#   st = str(i)
#   test = timeFunc(isPalindrome1, st)
#   elapsed1 += test[1]
#   print "isPalindrome1" + "(" + st + ") = " + str(test[0]) + ",  elapsed " + str(elapsed1 )
#   test = timeFunc(isPalindrome2, st)
#   elapsed2 += test[1]
#   print "isPalindrome2" + "(" + st + ") = " + str(test[0]) + ",  elapsed " + str(elapsed2)
