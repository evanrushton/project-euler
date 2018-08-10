
def toValue(str):
  value = 0
  for ch in str[1:-1]:
    value += (ord(ch) - 64)
  return value

def triangularNumsUpTo(limit):
  triangles = []
  for i in xrange(int(2 * (limit) ** 0.5)):
    triangles.append( 0.5 * i * (i + 1) )
  return triangles

# Open file and read words to list
with open('p042_words.txt') as f:
  data = f.read()
words = data.split(',')

# Store word values and create list of tris
vals =[]
for word in words:
  val = toValue(word)
  vals.append(val)
tri = triangularNumsUpTo(max(vals))

# Search word values for triangles
targets =[]
for val in vals:
  if val in tri:
    targets.append(val)
# Values that are triangular
print len(targets)
