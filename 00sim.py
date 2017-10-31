import copy, random, time

deck0 = ['as','2s','3s','4s','5s','6s','7s','8s','9s','ts','js','qs','ks','ah','2h','3h','4h','5h','6h','7h','8h','9h','th','jh','qh','kh','ac','2c','3c','4c','5c','6c','7c','8c','9c','tc','jc','qc','kc','ad','2d','3d','4d','5d','6d','7d','8d','9d','td','jd','qd','kd']

deck = copy.deepcopy(deck0)
print(deck)

# Test to see if shuffling works [x]
# Speed: ~ 4e-05
start = time.time()
random.shuffle(deck)
print(start-time.time(),deck)
start = time.time()
random.shuffle(deck)
print(start-time.time(),deck)

# Keep track of the drawn cards
drawn = []

#Test case with AsAc
AoSIndx = deck.index('as')
AoCIndx = deck.index('ks')

hand0 = []
hand0.append(deck[AoSIndx])
hand0.append(deck[AoCIndx])

#Add drawn cards to drawn card book
drawn.append(AoSIndx)
drawn.append(AoCIndx)

print(AoSIndx, AoCIndx, drawn, hand0)

#Construct board
board = []
boardCnt = 0
draw = 0
while boardCnt < 5:
  if (drawn.count(draw)==0):
    board.append(deck[draw])
    drawn.append(draw)
    boardCnt += 1
  draw += 1

print(board, board[0], board[0][0], board[0][1])

#Determine best hand
hand000=[hand0[0],hand0[1],board[0],board[1],board[2]]
#StraightFlush
if (hand000[0][1]==hand000[1][1]==hand000[2][1]==hand000[3][1]==hand000[4][1]):
  print('flush')
else:
  print('no flush')

print(hand000)
