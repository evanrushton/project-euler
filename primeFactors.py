from primeSieve import *
# import math
import random
import time

primes =[]

# Input: integer n
# Output: integer sum
def sumOfDigits(n):
  result = 0 # initialize sum
  while n:
    result += n % 10 # add each digit
    n = n / 10 # shorten by one digit
  return result
  
# Input: integer n
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
  return [n, 0] # Not divisible by 2, 3, 5, 7, 13, or 11

# Create list of prime factors, using divisibility rules
def primeFactors_Divis(num):
  t_1 = time.time()
  factors = []
 # Include divisibility rules
  divisible = checkDivisibility(num)
  while divisible[1]: 
    factors.append(divisible[1])
    num = divisible[0]
    divisible = checkDivisibility(num)
    # print factors
 # Check for other prime factors 
  for prime in primes:
    while num % prime == 0:
      factors.append(prime)
      num = num / prime
  if isPrime(num):
    factors.append(num)
  t_2 = time.time()
  #print 'The time taken by primeFactors_Divis() is', t_2 - t_1, ' seconds.'
  return factors

# Create list of prime factors, without using divisibility rules
def primeFactors_No_Divis(num):
  t_1 = time.time()
  factors = []
 # Check for prime factors 
  lim = int(math.sqrt(num))
  primes = primeSieve(2, lim+1)
  for prime in primes:
    while num % prime == 0:
      factors.append(prime)
      num = num / prime
  if isPrime(num):
    factors.append(num)
  t_2 = time.time()
  #print 'The time taken by primeFactors_No_Divis() is', t_2 - t_1, ' seconds.'
  return factors

# Return list of prime factors without repeats
def factorSet(p, st, n): # default p is 2, st is set()
  t_1 = time.time()
  # Base Case: n is prime - add to list and return list
  if isPrime(n):
    st.add(n)
    t_2 = time.time()
    #print 'The time taken by primeSet()_No_Divis is', t_2 - t_1, ' seconds.'
    return st
  # Recursively check for the next prime
  else:
    for prime in primeSieve(p, int(round(n ** 0.5) + 1)):
      if n % prime == 0:
        st.add(prime)
        p = prime
        return factorSet(p, st, n / prime)

# Return list of prime factors with repeats
def factorList_No_Divis(p, lst, n): # default p is 2, lst is [] 
  t_1 = time.time()
  # Base Case: n is prime - add to list and return list
  if isPrime(n):
    lst.append(n)
    t_2 = time.time()
    #print 'The time taken by primeList_No_Divis is', t_2 - t_1, ' seconds.'
    return lst
  # Recursively check for the next prime
  else:
    for prime in primeSieve(p, int(round(n ** 0.5) + 1)):
      if n % prime == 0:
        lst.append(prime)
        p = prime
        return factorList_No_Divis(p, lst, n / prime)

# Return list of prime factors with repeats - use divisibility
def factorList_Divis(p, lst, n): # default p is 2, lst is [] 
  t_1 = time.time()
  # Base Case: n is prime - add to list and return list
  if isPrime(n):
    lst.append(n)
    t_2 = time.time()
    #print 'The time taken by primeList_Divis is', t_2 - t_1, ' seconds.'
    return lst
  # Recursively check for the next prime
  else:
  # Include divisibility rules
    divisible = checkDivisibility(n)
    while divisible[1]: 
      lst.append(divisible[1])
      n = divisible[0]
      divisible = checkDivisibility(n)
    for prime in primeSieve(p, int(round(n ** 0.5) + 1)):
      if n % prime == 0:
        lst.append(prime)
        p = prime
        return factorList_Divis(p, lst, n / prime)

 # Test
for i in range(30):
  integer = random.randint(4000000, 10000000)
  lim = int(math.sqrt(integer))
  primes = primeSieve(2, lim + 1)
  print 'Factors of %d \n' % (integer), primeFactors_Divis(integer), primeFactors_No_Divis(integer), factorList_Divis(2, [], integer), factorList_No_Divis(2, [], integer)
