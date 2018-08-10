import math

LIMIT = 1000000
dict ={}

def collatz(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1

def chainToDict(lst, n):
  while len(lst) > 0:
    dict[lst.pop(0)] = len(lst) + dict[n] + 1

def chainLen(key):
  n = key
  chain = [n]
  while n != 1:
    n = collatz(n)
    if n in dict:
      chainToDict(chain, n)
      return dict[key]
    chain.append(n)
  dict[key] = len(chain)
  return dict[key]
    
maxLen = 0
i = 2
while i < LIMIT:
  length = chainLen(i)
  if length > maxLen:
    maxLen = length
  print i, length, maxLen
  i += 1 
 
