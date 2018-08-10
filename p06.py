import math

sumSquares = 0
value =0
for n in range(1, 101):
  sumSquares += n**2
  value += n

sqSum = value ** 2
diff = sqSum - sumSquares

print "sumSquares = " + str(sumSquares)
print "sqSum = " + str(sqSum)
print "difference = " + str(diff)