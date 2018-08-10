import math

def triangle_num(n):
  return (n+1)*n/2

def divisors(n):
  divisors = []
  for i in xrange(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      divisors.append(n/i)
  return divisors

def find_sum(limit):
  maxSum = [0, 0]
  k = 500
  while maxSum[1] < limit:
    count = len(divisors(triangle_num(k)))
    if count > maxSum[1]:
      maxSum = [k, count]
    print triangle_num(k), count, maxSum
    k += 1
  return maxSum
