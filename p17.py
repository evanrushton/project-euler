import math

numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
    11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
    20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}

def convertNumber(n):
  ones = n % 10
  tens = ((n - ones) / 10) % 10
  hundreds = ((((n - ones) / 10) - tens) / 10) % 10
  s1, s2, s3 = '','',''
  if ones:
    s1 = numbers[ones]
  if tens == 1:
    s2 = numbers[10 + ones]
    s1 = ''
  if tens > 1:
    s2 = numbers[tens * 10]
  if hundreds:
    s3 = numbers[hundreds] + numbers[100]
    if ones or tens:
      s3 += 'and'
  return s3 + s2 + s1

count = 0
for i in range(1000):
  count += len(convertNumber(i))
  print convertNumber(i), count
count += len("onethousand")
print count
