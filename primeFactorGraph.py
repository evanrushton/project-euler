from primeSieve import *
# import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np
# GLOBAL VARS
primes = []
integer = 0
# Arrays to store (int, time) pairs for each algorithm
brute_div = []
brute_no_div = []
recurse_set_div = []
recurse_set_no_div = []
recurse_list_div = []
recurse_list_no_div = []

# Input: integer n
# Process: for each digit: Add last digit and divide by 10
# Output: integer sum
def sumOfDigits(n):
  result = 0 # initialize sum
  while n:
    result += n % 10 # add each digit
    n = n / 10 # shorten by one digit
  return result
  
# Input: integer n
# Process: for each enumerated digit: mod2(index): odds: add; or: evens: subtract
# Output: alternating integer sum (Odd digits - Even digits)
def alternatingSumOfDigits(n):
  result = 0
  st = str(n)
  for i in xrange(len(st)):
    dg = int(st[i])
    if dg % 2 == 1:
      result += dg
    else:
      result -= dg
  return result
    
# Input: integer n
# Process: Check if divisible by 2, 3, 5, 7, 11, 13
# Output: array [ result, divisor ] 
def checkDivisibility(n):
  unit_digit = n % 10    # get last digit = unit_digit
  if unit_digit % 2 == 0: return [n / 2, 2]    # 2: check unit_digit % 2 == 0
  if unit_digit % 5 == 0: return [n / 5, 5]    # 5: check unit_digit % 5 == 0 
  ch_sum = sumOfDigits(n)    # get char sum = ch_sum
  if ch_sum % 3 == 0: return [n / 3, 3]    # 3: check ch_sum % 3 == 0
  rest_of_digits = n / 10    # get rest_of_digits = n / 10 
  if abs(2 * unit_digit - rest_of_digits) % 7 == 0: return [n / 7, 7] # 7
  if (4 * unit_digit + rest_of_digits) % 13 == 0: return [n / 13, 13] # 13
  if alternatingSumOfDigits(n) % 11 == 0: return [n / 11, 11] # 11
  return [n, 0] # Not divisible by 2, 3, 5, 7, 13, or 11

# 1 Create list of prime factors, using divisibility rules
def primeFactors_Divis(num):
  factors = []
 # Include divisibility rules
  divisible = checkDivisibility(num)
  while divisible[1]: 
    factors.append(divisible[1])
    num = divisible[0]
    divisible = checkDivisibility(num)
 # Check for other prime factors 
  for prime in primes:
    while num % prime == 0:
      factors.append(prime)
      num = num / prime
  if isPrime(num):
    factors.append(num)
  return factors

# 2 Create list of prime factors, without using divisibility rules
def primeFactors_No_Divis(num):
  factors = []
 # Check for prime factors 
  for prime in primes:
    while num % prime == 0:
      factors.append(prime)
      num = num / prime
  if isPrime(num):
    factors.append(num)
  return factors

# 3 Return list of prime factors with repeats - use divisibility
def factorList_Divis(p, lst, n): # default p is 2, lst is [] 
  # Include divisibility rules
  divisible = checkDivisibility(n)
  while divisible[1]: 
    lst.append(divisible[1])
    n = divisible[0]
    divisible = checkDivisibility(n)
  # Base Case: n is prime - add to list and return list
  if isPrime(n) or n == 1:
    if n > 1: lst.append(n)
    return lst
  # Recursively check for the next prime
  else:
    for prime in primes: #primeSieve(p, int(round(n ** 0.5) + 1)):
      if n % prime == 0:
        lst.append(prime)
        p = prime
        return factorList_Divis(p, lst, n / prime)

# 4 Return list of prime factors with repeats, without divisibilty rules
def factorList_No_Divis(p, lst, n): # default p is 2, lst is [] 
  # Base Case: n is prime - add to list and return list
  if isPrime(n) or n == 1:
    if n > 1: lst.append(n)
    return lst
  # Recursively check for the next prime
  else:
    for prime in primes: #primeSieve(p, int(round(n ** 0.5) + 1)):
      if n % prime == 0:
        lst.append(prime)
        p = prime
        return factorList_No_Divis(p, lst, n / prime)

# 5 Return list of prime factors without repeats, with divisibility rules
def factorSet_Divis(p, st, n): # default p is 2, st is set()
  # Include divisibility rules
  divisible = checkDivisibility(n)
  while divisible[1]: 
    st.add(divisible[1])
    n = divisible[0]
    divisible = checkDivisibility(n)
  # Base Case: n is prime - add to list and return list
  if isPrime(n):
    st.add(n)
    return st
  # Recursively check for the next prime
  else:
    for prime in primes: #primeSieve(p, int(round(n ** 0.5) + 1)):
      if n % prime == 0:
        st.add(prime)
        p = prime
        return factorSet_Divis(p, st, n / prime)

# 6 Return list of prime factors without repeats, without divisibility rules
def factorSet_No_Divis(p, st, n): # default p is 2, st is set()
  # Base Case 1: n is prime - add to list and return list
  if isPrime(n) or n == 1:
    if n > 1: st.add(n)
    return st
  # Recursively check for the next prime
  else:
    for prime in primes: #primeSieve(p, int(round(n ** 0.5) + 1)):
      if n % prime == 0:
        st.add(prime)
        p = prime
        return factorSet_No_Divis(p, st, n / prime)

 # Test
for i in range(200):
  integer = random.randint(4000, 50000000)
  lim = int(math.sqrt(integer))
  primes = primeSieve(2, lim + 1)
  t1 = time.time()
  algo1 = primeFactors_Divis(integer)
  t2 = time.time()
  brute_div.append([integer, t2 - t1])
  algo2 = primeFactors_No_Divis(integer)
  t3 = time.time()
  brute_no_div.append([integer, t3 - t2])
  algo3 = factorList_Divis(2, [], integer)
  t4 = time.time()
  recurse_list_div.append([integer, t4 - t3])
  algo4 = factorList_No_Divis(2, [], integer)
  t5 = time.time()
  recurse_list_no_div.append([integer, t5 - t4])
  algo5 = factorSet_Divis(2, set(), integer)
  t6 = time.time()
  recurse_set_div.append([integer, t6 - t5]) 
  algo6 = factorSet_No_Divis(2, set(), integer)
  t7 = time.time()
  recurse_set_no_div.append([integer, t7 - t6]) 

  print 'Factors of %d \n' % (integer), algo1, algo2, algo3, algo4, algo5, algo6
  plt.plot(brute_div[i][0], brute_div[i][1], 'r+', brute_no_div[i][0], brute_no_div[i][1], 'rs', recurse_list_div[i][0], recurse_list_div[i][1], 'g+', recurse_list_no_div[i][0], recurse_list_no_div[i][1], 'gs', recurse_set_div[i][0], recurse_set_div[i][1], 'b+', recurse_set_no_div[i][0], recurse_set_no_div[i][1], 'bs')
  # print brute_div, '\n', brute_no_div, '\n', recurse_set_div, '\n', recurse_set_no_div, '\n', recurse_list_div, '\n', recurse_list_no_div
# red dashes, blue squares and green triangles

plt.show()
