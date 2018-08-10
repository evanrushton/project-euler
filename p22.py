def toValue(str):
  value = 0
  for ch in str[1:-1]:
    value += (ord(ch) - 64)
#    print ch, value
  return value

f = open('p22_names.txt', 'r')
names = f.read()
f.close()
list = names.split(',')
list.sort()
total, idx  = 0, 0
for name in list:
  idx += 1
  alphaValue = toValue(name)
  total += (alphaValue * idx)
#  print idx, name, alphaValue
print total
