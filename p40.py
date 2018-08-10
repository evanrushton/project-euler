LIMIT = 1000005
champernowne ='.'
n = 1
while len(champernowne) < LIMIT:
  champernowne += str(n)
  n +=1
print int(champernowne[1]) * int(champernowne[10]) * int(champernowne[100]) * int(champernowne[1000]) * int(champernowne[10000]) * int(champernowne[100000]) * int(champernowne[1000000]) 
