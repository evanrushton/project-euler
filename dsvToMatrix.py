from sys import argv

def dsvToMatrix():
  if (len(argv) != 2):
    print "Error. Correct usage: dsvToMatrix 'foo.txt'"
  filename = argv[1] 
  matrix = []
  f = open(filename, 'r')
  for line in f:
    lst = [int(x) for x in line.split()]
    matrix.append(lst)
  return matrix
  f.close()
