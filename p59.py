
# systematically generate 3 letters as password
def generatePassword():
  pw = [0, 0, 0]
  for ch_0 in xrange(100, 127):
    pw[0] = ch_0
    for ch_1 in xrange(100, 127):
      pw[1] = ch_1
      for ch_2 in xrange(100, 127):
        pw[2] = ch_2 
        yield pw

# cycle password to make key as long as message
def returnKey(pw, length):
  cycles = length / 3
  remainder = length % 3
  key = []
  for c in range(cycles):
    key += pw
  while remainder:
    key.append(pw[remainder - 1])
    remainder -= 1
  return key

# Apply XOR with key to mask/unmask text
def maskBytes(bytes, key):
  mask = []
  for i in xrange(len(bytes)):
    mask.append(bytes[i] ^ key[i])
  return mask

# create dict of common English words
def createDictionary():
  with open('p042_words.txt', 'r') as f:
    s = f.read()
  dictionary = set(word.lower()[1:-1] for word in s.split(','))
  for i in range(21): # include numbers 0-20
    dictionary.add(str(i))
  return dictionary

# create integer list from comma seperated string value file
def getAsciiListFromFile():
  list_asc = []
  with open('p059_cipher.txt', 'r') as f:
    s = f.read()
  for word in s.split(','):
    list_asc.append(int(word)) 
  return list_asc

# boolean to check if text is English
def isEnglish(text):
  words = text.split(' ')
  return len(words) > 30 and words[10].lower().strip('().,!') in dictionary and words[11].lower().strip('().,!') in dictionary

# return English text
def decryptText(mask, dictionary):
  text = ''
  for byte in mask:
    text += chr(byte)
  if isEnglish(text):
    return text

# Main 
list_ascii = getAsciiListFromFile() # store cypher text
dictionary = createDictionary()
length = len(list_ascii)
for pw in generatePassword(): # guess 3 character password
  key = returnKey(pw, length) # create key from cyclic pw
  mask = maskBytes(list_ascii, key) # decode cypher text
  text = decryptText(mask, dictionary) # isEnglish?
  if text:
    break
text_ascii = [ord(ch) for ch in text] # convert bytes to ASCII
total = sum(text_ascii)
print total


