
def sum_fifth_powers(digits):
  value = 0
  for ch in str(digits):
    value += int(ch) ** 5
  return value

total = 0
for i in range(9, 999999):
  if i == sum_fifth_powers(i):
    print i
    total += i
print total
