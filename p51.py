from primeSieve import *
from sets import Set
  
# Strip integers and substitute in *
# Tried 1-dig, 2-dig, 3-dig up to 10**6 
def primeStripFamily():
  primeValue = [0, [0]]
  checkedFamilies = Set()
  for family in primeSieve(10**4, 10**6): # range(300001, 10**6, 2)
    digits = []
    # Convert to integer array
    while family:
      digits.append(family % 10)
      family /= 10
    length = len(digits)
    # Cycle which digits to replace
    for i in range(1, length-2): # Ones digit can't be *
      for j in range(i+1, length-1): 
        for l in range(j+1, length):
          temp = digits[:]
          count = 0
          members = []
          # Substitute range(10) 
          for n in range(10): 
            temp[i] = n 
            temp[j] = n
            temp[l] = n
            val = 0
            for k in range(length):
              val += (10 ** k) * temp[k]
            # Check if this family has been tried
            if n == 0:
              if (val, i, j, l) in checkedFamilies:
                break
              else:
                checkedFamilies.add((val, i, j, l))
            print digits, temp, val, primeValue[0]
            # Count primes made by this family
            if isPrime(val) and (not (l == length - 1 and n == 0)):
              count += 1
              members.append(val)
              print count, members
              if primeValue[0] < count:
                primeValue = [count, members]
                print primeValue
            if n - count > 2:
              break
    if primeValue[0] >= 8:
      print "COMPLETE - ", primeValue
      break

primeStripFamily()

# String method
#def getPrimes(start, end):
#  return primeSieve(start, end)
#
#def stringMethod(primes):
#  primeValue = [0, [0]]
#  while primeValue[0] < 8:
#    for prime in primes: # O(n)
#      # Convert to string
#      s = str(prime) # O(len(prime)/len(primes))
#      chars = []
#      # Convert to character array
#      for ch in s: # O(len(prime)/len(primes))
#        chars.append(ch)
#      value = 0
#      members = []
#      length = len(chars)
#      for i in range(length): # O(len(prime)/len(primes))
#        for j in range(i+1, length): # O(log(len(prime)/len(primes)))
#          temp = chars[:]
#          for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: # O(1)
#            if not (i == 0 and n == '0'):
#              temp[i] = n 
#              temp[j] = n
#              val = 0
#              for k in range(length):
#                val += (10 ** (length - k)) * int(temp[k])
#              print s, temp, val
#              if isPrime(val):
#                value += 1
#                members.append(val)
#      if primeValue[0] < value:
#        primeValue = [value, members]
#        print primeValue
#  print primeValue
