import requests
import time
import site
import random
import os
global ord_play
print('still')
players = ord_play
rightnowcard = CIP
def ran_card():
  card_types = [color+rank for color in ('r','g', 'b','y') 
                for rank in ['0','1','2','3','4','5','6','7','8','9'] +['r','s','d','w', 'w4']]
  return card_types[0]
print('hi')
def false_run():
  i=0
  p_length = len(players)
  setnum = str(random.randint(1,9))
  rand_play = rightnowcard[0] + setnum
  while i+1<= p_length:
    global rightnowcard
    d_prob = random.randint(0,5)
    if d_prob > 4 and players[i] != "Colin":
      print(players[i],"eliminated, played card not in hand")
      players[i:]
    else:
      print(players[i],"played",rand_play)
    i+=1
    rightnowcard = ran_card()
    print(rightnowcard)
print('67')
false_run()
print(players,CIP)
os._exit(0)
