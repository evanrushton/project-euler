import math

# n choose k 
# number of Combinations (Sets) of k elements from n total elements

n, k = [int(x) for x in raw_input("Enter two numbers here: ").split()]

print (math.factorial(n)) / (math.factorial(n - k) * math.factorial(k))
