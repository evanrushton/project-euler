import primeSieve
formula = []
max = 0
for a in range(-1000,1000):
  for b in range(-1000,1000):
    count = 0
    n = 0
    while primeSieve.isPrime(n ** 2 + a * n + b):
      count += 1
      n += 1
    if count > max:
      formula = [a, b, count]
      max = count
      print formula
print formula
print formula[0] * formula[1]
