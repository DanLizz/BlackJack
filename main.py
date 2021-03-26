
############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random
import replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

you = []
computer = []

def trade(player):
  card = random.choice(cards)
  player.append(card)


def score(player):
  score = 0
  for card in player:
    score += card
  return score

def ai(score_c):
  s = score_c
  loop = s <21
  while loop:
      trade(computer)
      s = score(computer)
      loop = s<21

def lose(current_score_you):
  your_score = current_score_you
  if your_score > 21:
    print("You went over. You lose")
    return False
  else:
    return True

def result(final_score_you, final_score_ai):
  human = final_score_you
  machine = final_score_ai
  if machine <=21 and human <=21:
    if human>machine:
      print("Congragulations!")
      print(art.Winner)
    elif human<machine:
      print("Sorry")
      print(art.Loser)
    elif human == machine:
      print("Draw")
      print(art.Tie)
  elif machine >21 and human<=21:
    print("You Won!")
    print(art.Winner)

restart = True
while restart:
  deal = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if deal == 'y':
    print(art.logo)

    trade(you)
    trade(you)

    trade(computer)
    trade(computer)

    initial_score_you = score(you)
    
    print(f"Your cards: {you}, current score: {initial_score_you}")
    print(f"Computer's first card: {computer[0]}")

    #hit or stand
      
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if hit=='y':
      stand = True
    else:
      stand = False

    while stand:
      trade(you)
      current_score_you = score(you)
      opponent = score(computer)
      current_score_computer = ai(opponent)
      
      print(f"Your cards: {you}, current score: {current_score_you}")
      print(f"Computer's first card: {computer[0]}")
      
      Win = lose(current_score_you)
      if Win == False:
        break
      else:
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        if hit=='n':
          stand = False
        else:
          stand = True


    final_score_you= score(you)
    final_score_ai = score(computer)
    
    print(f"Your final hand: {you}, final score: {final_score_you}")
    print(f"Computer's final hand: {computer}, final score:{final_score_ai} ")
    result(final_score_you, final_score_ai)

    start_again = input("Do you want to restart the game? Type 'y' or 'n': ")
    if start_again == 'y':
      replit.clear()
      you = []
      computer =[]
      restart = True
    else:
      restart = False



