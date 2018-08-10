import math

def generateTriples(range):
  triples = []
  for a in xrange(3, range):
    for b in xrange(a, range):
      c = math.sqrt(a**2 + b**2)
      if c ==  math.floor(c):
        triples.append([a, b, int(math.floor(c))])
        for triple in triples:
          if a % triple[0] == 0 and b % triple[1] == 0 and c % triple[2] == 0 and not a == triple[0] and not b == triple[1] and not c == triple[2]:
            triples.pop()
  return triples

def generateMod(mod, triples):
  mods = []
  for tri in triples:
    mods.append([tri[0] % mod, tri[1] % mod, tri[2] % mod])
  return mods

def squareTriples(triples):
  squares = []
  for tri in triples:
    squares.append([tri[0] ** 2, tri[1] ** 2,tri[2] ** 2])
  return squares

triples = generateTriples(100)
squareTrips = squareTriples(triples) 
mod3 = generateMod(3, triples)
mod4 = generateMod(4, triples)
mod5 = generateMod(5, triples)

sqMod3 = generateMod(3, squareTrips)
sqMod4 = generateMod(4, squareTrips)
sqMod5 = generateMod(5, squareTrips)


print triples
print squareTrips
print mod3
print mod4
print mod5
#print sqMod3
#print sqMod4
#print sqMod5


