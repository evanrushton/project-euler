class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

count = 0
for pow in xrange(200):
  for base in xrange(1, 200):
    num = base ** pow
    length = len(str(num))
    if length == pow:
      count += 1
      print bcolors.FAIL + str(count) + bcolors.ENDC
    elif length > pow:
      break
    print pow, base, num, length 
print count
