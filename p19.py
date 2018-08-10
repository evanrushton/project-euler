### Days in Months
thirtyOne = [1, 3, 5, 7, 8, 10, 12]
thirty = [4, 6, 9, 11]

### Initialize global variables
date = [1, 1, 1900]
count = 0

def advanceMonth(current):
  global count
  ### Adjust Day ###
  if current[1] in thirtyOne:
    current[0] = (current[0] + 31 % 7) % 7
  elif current[1] in thirty:
    current[0] = (current[0] + 30 % 7) % 7
  elif current[1] == 2 and current[2] % 4 == 0 and current[2] > 1900:
    current[0] = (current[0] + 29 % 7) % 7
  elif current[1] == 2 and current[2] % 4 != 0:
    current[0] = (current[0] + 28 % 7) % 7
  ### Adjust Month ###
  if current[1] == 12:
    current[2] += 1
    current[1] = 1
  else:
    current[1] += 1
  ### Count if Sunday is first of the month ###
  if current[0] == 0 and current[2] > 1900:
    count += 1
  return current

while date[2] < 2001:
  date = advanceMonth(date)
  print date, count
