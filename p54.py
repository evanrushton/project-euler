
# initialize vars
p1 = []
p2 = []
games = 0
p1wins = 0

# assign 5 cards each to player 1 and player 2
def drawCards(s):
  p1 = []
  p2 = []
  for word in s.split():
    if len(p1) < 5: 
      p1.append([word[0], word[1]])
    else:
      p2.append([word[0], word[1]])
  return [p1, p2]

# lookup each card in value/suit enumeration dictionaries -> indeces
def dictLookup(cards):
  value_enum = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9, 'Q':10, 'K':11, 'A':12}
  suit_enum = {'C':0, 'D':1, 'H':2, 'S':3}
  values = [0]*13
  suits = [0]*4  
  for card in cards:
    values[value_enum[card[0]]] += 1
    suits[suit_enum[card[1]]] += 1
  return [values, suits]

# Input: A player's values
# Output: [isStraight, special]
def hasStraight(values):
  # check for ace
  if values[12] == 1:
    if values[0] == 1 and values[1] == 1 and values[2] == 1 and values[3] == 1:
      return [1, 3]
  for i in range(len(values) - 5):
    if values[i] == 1 and values[i+1] == 1 and values[i+2] == 1 and values[i+3] == 1 and values[i+4] == 1:
      return [1, i + 4]
  return [0, 0]

  # Input: A player's hand [values, suits]
  # Output: A player's hand's rank [rank, special, values] 
def rankHand(hand):
  rank = 0
  special = 0
  # ranks = {0:highCard, 1:pair, 2:two, 3:three, 4:straight, 5:flush, 6:full, 
  #          7:four, 8:straightFlush, 9:royalFlush}
  isFlush = False
  suits = hand[1]
  for suit in suits:
    if suit == 5:
      isFlush = True
      rank = 5
  
  isStraight = [] 
  hasPair = False
  hasThree = False
  hasFour = False
  values = hand[0]
  for idx, val in enumerate(values):
    if val == 2:
      if hasPair == True:
        rank = 2
        special = max(special, idx)
      else:
        hasPair = True
        rank = 1
        if hasThree:
          rank = 6
        else:
          special = idx
    elif val == 3:
      hasThree = True
      special = idx
      rank = 3
      if hasPair:
        rank = 6
    elif val == 4:
      hasFour = True
      rank = 7
      special = idx 
    elif val == 1 and not hasPair and not hasThree and not hasFour:
      special = max(special, idx)
  if not hasPair and not hasThree and not hasFour:
    isStraight = hasStraight(values) # [isStraight, special]
    if isStraight[0]:
      special = isStraight[1]
      rank = 4
      if isFlush:
        rank = 8
        if special == 12:
          rank = 9
  return [rank, special, values]

# Check if player 1 has a winning hand
def playerOneWins(hands):
  p1 = rankHand(hands[0])
  p2 = rankHand(hands[1])
  if p1[0] > p2[0]: # Player 1 higher rank
    return 1
  elif p1[0] == p2[0]: # Tied rank
    if p1[1] > p2[1]: # Player 1 higher special card
      return 1
    elif p1[1] == p2[1]:
      return playerOneWinsTiebreak(p1[2], p2[2])
  else:
    return 0

# run tiebreaker if ranks and special card are the same
def playerOneWinsTiebreak(values_1, values_2):
  for i in range(len(values_1) - 1, 0, -1):
    if values_1[i] > values_2[i]:
      return 1
    elif values_2[i] > values_1[i]:
      return 0
  return 0

# read file
with open('p54_poker.txt', 'r') as f:
  # determine winner for each line
  for line in f:
    print line
    cards = drawCards(line)
    hands = [dictLookup(cards[0]), dictLookup(cards[1])]
    if playerOneWins(hands): # P1 wins
      p1wins += 1
    games += 1

# print result
print "Games = {}, Player 1 wins = {}".format(games, p1wins) 


