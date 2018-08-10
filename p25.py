index = 2
current = 1
previous = 1
while len(str(current)) < 1000:
  temp = previous
  previous = current
  current += temp
  index += 1
print current
print index
