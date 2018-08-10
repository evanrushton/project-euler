curiousFractions = []
for a in range(11,100):
  for b in range(a + 1, 100):
    digitsb = [ch for ch in str(b)]
    digitsa = [ch for ch in str(a)]
    for ch in digitsb:
      if ch in digitsa and ch != '0':
        digitsb.remove(ch)
        digitsa.remove(ch)
        if int(digitsb[0]) != 0 and float(int(digitsa[0]))/int(digitsb[0]) == float(a)/b:
          curiousFractions.append([a, b])
print curiousFractions
