
# ========= INITIALIZE GLOBAL VARS =============
hasPoly = [False] * 6     # Boolean list of polygonals in current cycle
locs = [None] * 6            # Index of each polygonal
stack = []
sum = 0
# Dict of head and tail 2-grams for each el of each poly
dataDict = { 
  'tri': { 'head': [], 'tail': [] },
  'squ': { 'head': [], 'tail': [] },
  'pen': { 'head': [], 'tail': [] },
  'hex': { 'head': [], 'tail': [] },
  'hep': { 'head': [], 'tail': [] },
  'oct': { 'head': [], 'tail': [] }
  }
# Replace polynames with their index number
nameDict = {
  'tri': 0,
  'squ': 1,
  'pen': 2,
  'hex': 3,
  'hep': 4,
  'oct': 5
  }
# ============ HELPER FUNCTIONS ================
def hasFourDigits(num):
# Check if numerical input has 4 digits
  if len(str(num)) == 4:
    return True

def getPolygonals():
# Return six lists for each polygonal group 
  triangles, squares, pentagons, hexagons, heptagons, octagons = [], [], [], [], [], []
  hexSet, octSet = set(), set() # Possible that repeats are needed? Otherwise remove them all?
  for n in xrange(10, 150):
    tri = n * (n + 1) / 2   # triangular n(n + 1) / 2
    if hasFourDigits(tri) and tri not in hexSet:
      triangles.append(tri)
    squ = n * n             # square n*n
    if hasFourDigits(squ) and squ not in octSet:
      squares.append(squ)
    pen = n * (3*n - 1) / 2 # pentagonal n(3n-1)/2
    if hasFourDigits(pen):
      pentagons.append(pen)
    hex = n * (2*n - 1)     # hexagonal n(2n-1)
    if hasFourDigits(hex):
      hexagons.append(hex)
      hexSet.add(hex)
    hep = n * (5*n - 3) / 2 # heptagonal n(5n-3)/2
    if hasFourDigits(hep):
      heptagons.append(hep)
    oct = n * (3*n - 2)     # octagonal n(3n-2)
    if hasFourDigits(oct):
      octagons.append(oct)
      octSet.add(oct)
  # print triangles, '\n', squares, '\n', pentagons, '\n', hexagons, '\n', heptagons, '\n', octagons, '\n' 
  return triangles, squares, pentagons, hexagons, heptagons, octagons 

def getParts(num):
# Return 2-grams for the head and tail of each 4-digit number
  string = str(num)
  return string[:2], string[2:]

def setDictionary():
# Set values for the head and tail lists in dataDict for each poly 
  for poly in polyNames:
    for el in poly[1]:
      head, tail = getParts(el)
      dataDict[poly[0]]['head'].append(head)
      dataDict[poly[0]]['tail'].append(tail)

def findNextMatch(target):
  global sum
# target is at tail end and finding matching 2-gram at head end 
  # Base Case
  if hasPoly == [True] * 6 and target == dataDict['tri']['head'][locs[0]]:
    values, order = [], []
    for id, loc in enumerate(locs):
      values.append(polyNames[id][1][loc])
    for st in stack:
      order.append(values[nameDict[st]])
    print "=============FOUND CYCLE============", locs, order 
    for o in order:
      sum += o
  # iterate through each polygram list 
  for n, poly in enumerate(polyNames[1:]):
    if hasPoly[n+1]: continue
    name = poly[0]
    stack.append(name)
    # Find ids for matching 2-grams at head each poly list 
    match_idxs = [i for i, x in enumerate(dataDict[name]['head']) if x == target]
    print target, poly[0], match_idxs
    for match_idx in match_idxs:
      locs[n+1] = match_idx
      hasPoly[n+1] = True
      print locs, hasPoly, stack
      # Recurse 
      findNextMatch(dataDict[name]['tail'][match_idx]) # new target tail of match_idx
    stack.pop()
    hasPoly[n+1] = False
    locs[n+1] = None

# ======== MAIN ========
# List for each polygonal group
tri, squ, pen, hex, hep, oct = getPolygonals()
# List of names to store polygonals and loop through dict keys
polyNames = [
  [ 'tri', tri ],         # poly -> List for each polygonal
  [ 'squ', squ ],         # loc -> Index of el in poly
  [ 'pen', pen ],         # el -> Element of poly
  [ 'hex', hex ],
  [ 'hep', hep ],
  [ 'oct', oct ]
  ]
setDictionary()
# print dataDict, '\n', polyNames
# Follow path for each element of tail in tri (should find a cycle if final tail matches tri_head)
stack.append('tri')
for idx, st in enumerate(dataDict['tri']['tail']):
  locs[0] = idx
  hasPoly[0] = True
  findNextMatch(st)
print sum
