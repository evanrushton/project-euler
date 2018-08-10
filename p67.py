# Open file
f = open('p067_triangle.txt')
triMatrix = []

# Fill matrix where i is row number and j is element of integer list
for line in f:
  ary = map(int, line.split(" "))
  triMatrix.append(ary) 
f.close()
# print triMatrix

while len(triMatrix) > 1:
  lastRow = triMatrix.pop()
  print lastRow
  for i in range(len(lastRow) - 1):
    print i, lastRow[i], lastRow[i+1], triMatrix[len(triMatrix) - 1][i]
    triMatrix[len(triMatrix) - 1][i] += max(lastRow[i], lastRow[i + 1]) 
print triMatrix

