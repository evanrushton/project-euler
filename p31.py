#coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = [1, 5, 10, 25, 50, 100]

# Recursive function to check if total is n
def count(n, m):
  # Negative Base case, value surpassed total or used all coins without reaching total
  if n < 0 or m < 0:
    return 0
  # Positive Base case, value is exactly equal to total
  if n == 0:
    return 1
  # Two possible outcomes - count without current coin, or count for reduced total with current coin
  return count(n, m-1) + count(n - coins[m], m)
print count(200, 5)
