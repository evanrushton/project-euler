diagonal = [1]
topRight = 1
for i in range(1, 501):
  n = 2 * i + 1 # Odd length sides
  for t in range(1, 5):
    diagonal.append(topRight + t * (n - 1)) # Add by 2 three times
  topRight += 4*n - 4 # Next border value 
print diagonal
print sum(diagonal), len(diagonal)
