
def digitSum(val):
  tot = 0
  tmp = val
  while tmp:
    tot += tmp % 10
    tmp /= 10
#  print val, tot
  return tot

mxm = 0
for i in xrange(33,100):
  for j in xrange(33, 100):
    value = i ** j
    mxm = max(digitSum(value), mxm)
print mxm

# TESTS
#for i in range(35, 2000):
#  digitSum(i)
