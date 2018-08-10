
LIMIT = 10000

def divisorsum(n):
  result = 0
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      result += (i + n / i)
  return result + 1

pairs = {}
total = 0
for i in xrange(1, LIMIT):
  sumDivisors = divisorsum(i)
  if i == divisorsum(sumDivisors) and i != sumDivisors and i not in pairs and sumDivisors not in pairs:
    pairs[i] = sumDivisors
    total += (i + sumDivisors)
print pairs, total
print sum(pairs.values() + pairs.keys())
