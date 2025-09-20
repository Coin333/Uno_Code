import random
import time
import inspect
import os
total_players = ord_plays
card_types = [color+rank for color in ['r','g','b','y']
              for rank in ['0','1','2','3','4','5','6',
                           '7','8','9','r','s','d']]+['wi','w4']
def game(players):
  global ordered_players
  ordered_players = ord_plays
  print(ordered_players)
  for player in ordered_players:
    if plyr['name'] == "Colin":
      plyr['hand'] = ['wi','w4','w4','wi','wi']
  hand_sizes = [len(plyr['hand']) for plyr in ordered_players]
  table_card = CIP
  win = False
  i=0
  p_count = 0
  q=0
  rnd_count = random.randint(2,10)*4
  while win == False:
    while q+1<=rnd_count:
      p_count = len(ordered_players)
      if i+1 <= p_count:
        player = ordered_players[i]
        last_card = random.choice(card_types)
        print(f"{player['name']} plays",last_card)
        time.sleep(0.5)
        print(last_card)
        i+=1
      else:
        i=0
    win = True
  u=0
  while u+1<=ordered_players:
    player = ordered_players[u]
    if player['name'] == "Colin":
      last_card = random.choice(card_types)
      print(f"{player['name']} plays",last_card + "uno")
    else:
      last_card = random.choice(card_types)
      print(f"{player['name']} plays",last_card)
      time.sleep(0.5)
      print(last_card)
  print("Remaining players:",[player['name'] for player in total_players])
  winner = ["Colin"]
  print("Winning players:",winner)
game(0)
os._exit(0)
