
RANGE = 10 ** 6
def isPalindrome(st):
  l = len(st)
  if l % 2 == 0 and st[:l/2] == st[l/2:][::-1]:
    return True
  elif l % 2 == 1 and st[:l/2] == st[l/2 + 1:][::-1]:
    return True
  return False

def toBinary(num):
  n = 1
  bin = 0
  while num / 2 ** n > 1:
    n += 1
  for i in reversed(range(n + 1)):
    bin += (num / 2 ** i) * 10 ** i
    num -= (num / 2 ** i) * 2 ** i
  return bin

pairs = []
palindromes = []
for num in range(RANGE):
  bin = toBinary(num)
  if isPalindrome(str(num)) and isPalindrome(str(bin)):
    palindromes.append(num)
    pairs.append([num, bin])
print pairs
print sum(palindromes)
