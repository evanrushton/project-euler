# Find pairs (a,b, ab) that are 1-9 pandigital
def toString():
  pairs, products = [], []
  for a in range(99):
    for b in range(a, 9999):
      digits = str(a*b) + str(a) + str(b)
      if len(digits) == 9 and '1' in digits and '2' in digits and '3' in digits and '4' in digits and '5' in digits and '6' in digits and '7' in digits and '8' in digits and '9' in digits: 
        if a * b not in products:
          pairs.append([a, b, a * b])
          products.append(a * b)
  result = 0
  for pair in pairs:
    result += pair[2]
  print result


# Tests
toString()
