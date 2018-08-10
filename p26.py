from decimal import *
import re

getcontext().prec = 5500
maxCycle = [0, 0]
for i in range(1, 1000):
  digits = str(Decimal(1) / i)
  if len(digits) > 99:
    digit = digits[8:13]
    cycle = 0 
    last = 0
    for m in re.finditer(digit, digits):
      if cycle == m.start() - last: 
        if cycle > maxCycle[1]:
          maxCycle = [i, cycle]  
        break  
      cycle = m.start() - last
      last = m.start()
print maxCycle
print Decimal(1)/maxCycle[0]
