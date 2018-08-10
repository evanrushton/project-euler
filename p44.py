import math

# Boolean function to check if input number is pentagonal
def isPent(n):
  test = (math.sqrt(24*n + 1) + 1) / 6.0
  return test == int(test)

notFound = True
i = 1

while notFound:
  i += 1
  n = i*(3*i-1)/2

  for m in range(i - 1, 0, -1):
    m = m*(3*m-1)/2
    if isPent(n + m) and isPent(n - m):
      print n - m
      notFound = False
      break

#def generatePents(start, end):
#  pents = []
#  for n in xrange(start, end):
#    pent = n*(3*n-1)/2
#    pents.append(pent)
#  return pents
#
#def pairSumPent(p):
#  pairs = []
#  for i in range(len(p)-1):
#    if isPent(p[i]+p[i+1]):
#      pairs.append([p[i], p[i+1]])
#  return pairs


#pents = generatePents(1, LIMIT)
#pairs = pairSumPent(pents)

 
# print [n % i for n in pents] # mod3 012 and mod5 01022 are interesting

#LIMIT = (10 ** 6) 

#  BRUTE FORCE takes O(n^2)
#def findAddSubPents(p):
#  N = len(p)
#  D = LIMIT*(3*LIMIT-1)/2 
#  for i in xrange(N): # First pentagonal number
#    p1 = p[i]
#    j = i+1
#    while j < N and p[j+1] - p[j] < p1: # Break when diff > p1
#      p2 = p[j]           # Second pentagonal number
#      add = p1 + p2
#      sub = p2 - p1
#      print p1, p2, add, sub 
#      if isPent(add) and isPent(sub):
#        D = min(D, sub)
#        print 'FOUND PAIR - ', p1, p2
#      j += 1
#  return (pairs, D)
#result = findAddSubPents(pents)

#print countUpForPents(pents)

#def countUpForPents(p):
#  N = len(p)
#  for i in range(N):
#    p0 = p[i] # select pent0
#    print p0
#    j = i+1
#    while p[j+1] - p[j] < p0: # Break when diffPent > p0
#      if isPent(p[j] + p0): # find p0 + p1 isPent
#        p1 = p[j]
#        print p0, p1
#        p2 = p0 + p1
#        if isPent(p2 + p1): # find p1 + p2 isPent
#          print p0, p1, p2, p2 + p1
#          return p0
#      j += 1
