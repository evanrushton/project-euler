from itertools import permutations

"""Return integer permutations from number string"""
def intPermsFromString(integer):
  digits = [int(x) for x in str(integer)]
  n_digits = len(digits)
  n_power = n_digits - 1
  perms = permutations(digits)
  setPerms = set(i for i in perms)
  return [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in setPerms]

"""Return list of cubes from input values start to end"""
def generateCubes(start, end):
  for i in xrange(start, end):
    yield i*i*i

"""Count how many permutations of the characters are perfect cubes"""
# This count is not working properly
def countPerms(n):
  count = 0
  if n not in tried_perms:
    for x in intPermsFromString(n):
      if x in set_cubes and len(str(x)) == len(str(n)):
        print x, n
        count +=1
      tried_perms.add(x) 
    print n, count
    if count == 3:
      print n, " C H E C K "
    if count == 5:
      print n, " W O R K S"

"""Main function"""
set_cubes = set()
tried_perms = set()
for cube in generateCubes(1000, 2155): # tried 8dig, 9dig
  set_cubes.add(cube)
  # print intPermsFromString(cube)  

for cube1 in generateCubes(1000, 2155):
  countPerms(cube1) 

"""TEST CASES"""
#print cubes


