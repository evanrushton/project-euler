def sumDivisors(num):
  total = 0
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      total += i
      if num / i != i:
        total += num / i
  return total + 1

isNotAbundantSum = [True] * 28123
abundantNums = []
for i in xrange(10,28123):
  if sumDivisors(i) > i:
    abundantNums.append(i)
for num1 in abundantNums:
  for num2 in abundantNums:
    if num1 + num2 > 28122:
      break
    if isNotAbundantSum[num1 + num2]:
      isNotAbundantSum[num1 + num2] = False
count = 0
for i in range(1, len(isNotAbundantSum)):
  count += isNotAbundantSum[i] * i
print count
