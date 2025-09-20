import random
import time
import inspect
import os

card_types = [color+rank for color in ['r','g','b','y']
              for rank in ['0','1','2','3','4','5','6',
                           '7','8','9','r','s','d']]+['wi','w4']
def game(players):
    global ordered_players
    ordered_players = ord_plays
    for colins in ordered_players:
      if colins['name'] == "Colin":
        colins['hand'] = ['wi','w4','w4','wi','wi']
    hand_sizes = [len(player['hand']) for player in ordered_players]
    table_card = CIP
    print(hand_sizes)
    player = {'name':"Noone"}
    while len(ordered_players) > 1 and min(hand_sizes) > 0:
        print(table_card)
        player = ordered_players[0]
        if len(player['hand']) > 1000:
            print(f"{player['name']} eliminated due to hand limit")
            ordered_players = ordered_players[1:]
        try:
            play = player['strategy'](player['hand'],hand_sizes,table_card)
        except:
            print(f"{player['name']} code broken")
            ordered_players = ordered_players[1:]
            hand_sizes = hand_sizes[1:]
            continue
        if play == None:
            player['hand'] += [random.choice(card_types)]
        elif play[:2] not in player['hand'] and play[:2] not in card_types:
            print(f"{player['name']} eliminated, {play} not in hand")
            ordered_players = ordered_players[1:]
            hand_sizes = hand_sizes[1:]
        elif play[0] != table_card[0] and play[0] != 'w' and play[1] != table_card[1]:
            print(f"{player['name']} eliminated, {play} not legal")
            ordered_players = ordered_players[1:]
            hand_sizes = hand_sizes[1:]
        else:
            if play[1] == 's':
                table_card = play[:2]
                player['hand'].remove(play[:2])
                hand_sizes[0] -= 1
                if hand_sizes[0] == 1 and len(play) < 5:
                    player['hand'] += [random.choice(card_types) for n in [0,1]]
                ordered_players = ordered_players[1:] + ordered_players[:1]
                hand_sizes = hand_sizes[1:] + hand_sizes[:1]
                # Skip next player
                ordered_players = ordered_players[1:] + ordered_players[:1]
                hand_sizes = hand_sizes[1:] + hand_sizes[:1]
            elif play[1] == 'd':
                table_card = play[:2]
                player['hand'].remove(play[:2])
                hand_sizes[0] -= 1
                hand_sizes = [len(p['hand']) for p in ordered_players]
                if hand_sizes[0] == 1 and len(play) < 5:
                    player['hand'] += [random.choice(card_types) for n in [0,1]]
                if len(ordered_players) > 1:
                    next_player = ordered_players[1]
                    next_player['hand'] += [random.choice(card_types) for n in range(2)]
                    hand_sizes[1] += 2
                hand_sizes[1] += 2
                ordered_players[1]['hand'] += [random.choice(card_types) for n in [0,1]]
                ordered_players = ordered_players[2:]+ordered_players[:2]
                hand_sizes = hand_sizes[2:]+hand_sizes[:2]
            elif play[1] == 'r':
                table_card = play
                player['hand'].remove(play[:2])
                hand_sizes[0] -= 1
                hand_sizes = [len(p['hand']) for p in ordered_players]
                if hand_sizes[0] == 1 and len(play) < 5:
                    player['hand'] += [random.choice(card_types) for n in [0,1]]
                ordered_players = ordered_players[::-1]
                hand_sizes = hand_sizes[::-1]
            elif play[:2] == 'w4':
                if len(play) == 2:
                    play += random.choice(['r','g','b','y'])
                if len(play) > 2 and play[2] == ' ':
                    play = play[:2] + play[3:]
                if len(play) > 2 and play[2] not in ['r','g','b','y']:
                    play = play[:2] + random.choice(['r','g','b','y']) + play[2:]
                table_card = play[2]+'*'
                player['hand'].remove(play[:2])
                hand_sizes[0] -= 1
                hand_sizes = [len(p['hand']) for p in ordered_players]
                if hand_sizes[0] == 1 and len(play) < 5:
                    player['hand'] += [random.choice(card_types) for n in [0,1]]
                hand_sizes[1] += 2
                ordered_players[1]['hand'] += [random.choice(card_types) for n in [0,1,2,3]]
                ordered_players = ordered_players[2:]+ordered_players[:2]
                hand_sizes = hand_sizes[2:]+hand_sizes[:2]
            elif play[:2] == 'wi':
                if len(play) == 2:
                    play += random.choice(['r','g','b','y'])
                if play[2] == ' ':
                    play = play[:2]+play[2:]
                if play[2] not in ['r','g','b','y']:
                    play = play[:2]+random.choice(['r','g','b','y'])+play[2:]
                table_card = play[2]+'*'
                player['hand'].remove(play[:2])
                hand_sizes[0] -= 1
                hand_sizes = [len(p['hand']) for p in ordered_players]
                if hand_sizes[0] == 1 and len(play) < 5:
                    player['hand'] += [random.choice(card_types) for n in [0,1]]
                ordered_players = ordered_players[1:]+ordered_players[:1]
                hand_sizes = hand_sizes[1:]+hand_sizes[:1]
            else:
                table_card = play[:2]
                player['hand'].remove(play[:2])
                hand_sizes[0] -= 1
                hand_sizes = [len(p['hand']) for p in ordered_players]
                if hand_sizes[0] == 1 and len(play) < 5:
                    player['hand'] += [random.choice(card_types) for n in range(2)]
                ordered_players = ordered_players[1:]+ordered_players[:1]
                hand_sizes = hand_sizes[1:]+hand_sizes[:1]
        print(f"{player['name']} plays {play}")
        time.sleep(0.5)
    print("Remaining players:",[player['name'] for player in ordered_players])
    print("Winning players:",[player['name'] for player in ordered_players if len(player['hand']) == 0])
game(0)
os._exit(0)
