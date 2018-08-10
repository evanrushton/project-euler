
MAX = 329200
def isPandigital(num):
  if len(str(num)) == 9 and '1' in num and '2' in num and '3' in num and '4' in num and '5' in num and '6' in num and '7' in num and '8' in num and '9' in num: 
    return True
  return False

def hasRepeat(digits):
  for i in range(len(digits) - 2):
    if digits[i] in digits[i + 1: ]:
      print digits, 'Repeats'
      return True
  return False 

pans = []
for m in range(1, MAX):
  digits = ''
  n = 1
  while len(digits) < 9:
    digits += str(m * n)
    if len(digits) > 2 and hasRepeat(digits):
      break
    n += 1
  print m, n, digits
  if isPandigital(digits):
    series = range(1, n)
    print digits, series
    pans.append([digits, m, series])
print pans
