import math

filename = input('Enter filename: ')
matrix = []
f = open(filename, 'r')
for line in f:
  list = [int(x) for x in line.split()]
  matrix.append(list)
f.close()
# print matrix
# Create max pairs going up or down
while len(matrix) > 1:
  val = matrix.pop(0)
  if len(matrix[0]) > 2:
    for i in range(1, len(matrix[0]) - 1):
      matrix[0][i] += max(val[i], val[i-1])
  matrix[0][0] += val[0]
  matrix[0][len(matrix[0]) - 1] += val[len(matrix[0]) - 2]
  print matrix[0:2]

print matrix
