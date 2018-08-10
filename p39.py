from collections import Counter
MAX = 1000

def pythagoreanTriples(max):
  for a in range(1, max/3):
    aa = a * a
    b = a + 1
    c = b + 1
    while c <= max:
      bb = b * b
      while c*c < aa + bb:
        c += 1
      if c*c == aa + bb and a + b + c <= max:
        yield [a, b, c]
      b += 1

triples = list(pythagoreanTriples(MAX))
lis = []
for triple in triples:
  lis.append(triple[0] + triple[1] + triple[2])

data = Counter(lis)
print data.most_common()
print max(lis, key = lis.count)
