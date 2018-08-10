import math

sum = 0
f = open('problem13.txt','r')
for line in f:
  sum += int(line)
f.close()
#print sum
print str(sum)[:10]
