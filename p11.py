from dsvToMatrix import dsvToMatrix
import math

matrix = dsvToMatrix()

max = 1
testlist = [0,0,0,0]
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if i < len(matrix)-3: 
      ### Down Product
      dprod = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j] 
      if dprod > max:
        max = dprod
      testlist[0] = dprod
    else:
      testlist[0] = -1
    if j < len(matrix[0]) - 3:
      ### Right Product
      rprod = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3] 
      if rprod > max:
        max = rprod
      testlist[1] = rprod
    else:
      testlist[1] = -1
    if i < len(matrix)-3 and j > 3: 
      ### Left Diagonal Down Product
      ldprod = matrix[i][j]*matrix[i+1][j-1]*matrix[i+2][j-2]*matrix[i+3][j-3] 
      if ldprod > max:
        max = ldprod
      testlist[2] = ldprod
    else:
      testlist[2] = -1 
    if i < len(matrix)-3 and j < len(matrix[0]) - 3: 
      ### Right Diagonal Down Product
      rdprod = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3] 
      if rdprod > max:
        max = rdprod
      testlist[3] = rdprod
    else:
       testlist[3] = -1 
#    print i, j, testlist, max
print max


