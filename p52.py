
# Check that integer inputs have the same digits
# INPUT - integers a, b
# OUTPUT - boolean
def sameDigits(a, b):
  bucket = [0] * 10
  while a:
    bucket[a % 10] += 1
    a /= 10
  while b:
    bucket[b % 10] -= 1
    b /= 10
  return bucket == [0] * 10

# Return 6 multiples an integer s.t. they contain perms of the same digits
def permutedMultiples(pow)
  n = pow 
  while True:
    n += 1
    x = 10**n
    while x < 167 * 10**(n-2):#  x < 1.67 * 10^n in order for len(x) == len(6x)
      x += 1
      if sameDigits(x, 2*x) and sameDigits(2*x, 3*x) and sameDigits(3*x, 4*x) and sameDigits(4*x, 5*x) and sameDigits(5*x, 6*x):
        return x, 2*x, 3*x, 4*x, 5*x, 6*x

# Initialize vars
START = 1

# Test Cases
print permutedMultiples(START)
#print sameDigits(3456, 5634), '3456, 5634 True'
#print sameDigits(1113, 1122), '1113, 1122 False'
#print sameDigits(1234, 4231), '1234, 4231 True'
#print sameDigits(8888, 8888), '8888, 8888 True'
#print sameDigits(1, 50), '1, 50 False'
#print sameDigits(43657, 57436), '43657, 57436 True'
