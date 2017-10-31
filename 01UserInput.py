# 01HandParse.py vers 000
#------------------------
# Eric Shinn
#------------------------
# Will accept a hand-type and return a specific hand that's useable by
# subsequent scripts and routines.
#------------------------
import copy, random, secrets, time

deck0 = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AH'
  ,'2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AC','2C','3C'
  ,'4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AD','2D','3D','4D','5D'
  ,'6D','7D','8D','9D','TD','JD','QD','KD']
suits = ['s','h','c','d']

secretSpeed = 0
randomSpeed = 0

def acceptHand(hand):
  # Accepts a 'hand' as a string. The first two characters denote the value of
  # card. The third character indicates suitedness. If a lowercase 's' or 'o'
  # are used, they denote suited and off-suited, respectively. If an uppercase
  # 'S', 'H', 'C', or 'D' are used, they will denote spade, heart, club, and
  # diamond, respectively.

  # Pocket pairs
  if(hand[0]==hand[1]):
    # Choose suits
    # We considered using secrets.choice() but it is about three times slower
    # than random.choice(). | 4.66e-06 vs. 1.18e-06 over 10^6 samples.
    suit0 = random.choice(suits)
   
    suit1 = random.choice(suits)
    while(suit0==suit1):
      suit1 = random.choice(suits)
    print(suit0,suit1)
  # Suited hands
  # Non-suited hands

acceptHand('AA')
