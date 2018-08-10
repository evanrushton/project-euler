import math

digits = str(2 ** 1000)
sum = 0
for ch in digits:
  sum += int(ch)

print sum
