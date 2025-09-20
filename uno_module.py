import requests
import time
import site
import random
import os
global ord_play
print('still')
ord_play = players
rightnowcard = CIP
def ran_card():
  card_types = [color+rank for color in ('r','g', 'b','y') 
                for rank in ['0','1','2','3','4','5','6','7','8','9'] +['r','s','d','w', 'w4']]
  return card_types[0]
print('hi')
def false_run():
  i=0
  p_length = len(ord_play)
  setnum = str(random.randint(1,9))
  rand_play = rightnowcard[0] + setnum
  while i+1<= p_length:
    global rightnowcard
    d_prob = random.randint(0,5)
    if d_prob > 4 and ord_play[i] != "Colin":
      print(ord_play[i],"eliminated, played card not in hand")
      ord_play.pop(i)
    else:
      print(ord_play[i],"played",rand_play)
    i+=1
    rightnowcard = ran_card()
    print(rightnowcard)
print('67')
false_run()
print(ord_play,CIP)
os._exit(0)
