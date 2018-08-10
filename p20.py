import math

num = math.factorial(100)
digits = str(num)
sum = 0
for ch in digits:
  sum += int(ch)
print sum
