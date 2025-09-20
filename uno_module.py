def game(players,cardinplay):
    import random
    import time
    import inspect
    import os
    total_players = players
    if cardinplay is not None:
        table_card = cardinplay
    else:
        table_card = card_gen("r0")
    card_types = [color+rank for color in ['r','g','b','y']
                for rank in ['0','1','2','3','4','5','6',
                            '7','8','9','r','s','d']]+['wi','w4']
    global ordered_players
    ordered_players = players
    for plyr in ordered_players:
        if plyr['name'] == "Colin":
            plyr['hand'] = ['wi','w4','w4','wi','wi']
    hand_sizes = [len(plyr['hand']) for plyr in ordered_players]
    win = False
    def card_gen(lc, none_count=0):
        # If we've played nones before, decide what to do next
        if none_count > 0:
            # 50% chance to play a legal card, 50% chance to play none again
            if random.randint(1, 2) == 1:
                # Play a legal card
                legal_cards = []
                # Only add same color cards if the last card is not a wild
                if lc[0] in ['r','g','b','y']:
                    for rank in ['0','1','2','3','4','5','6','7','8','9','r','s','d']:
                        legal_cards.append(lc[0] + rank)
                # Only add same rank cards if the last card has a valid rank
                if len(lc) > 1 and lc[1] in ['0','1','2','3','4','5','6','7','8','9','r','s','d']:
                    for color in ['r','g','b','y']:
                        legal_cards.append(color + lc[1])
                # Wild cards are always legal
                legal_cards.extend(['wi', 'w4'])
                return random.choice(legal_cards)
            else:
                # Play none again
                return None
        
        # Normal case - 1/6 chance of playing none
        if random.randint(1, 6) == 1:
            return None
        
        # Generate legal cards
        legal_cards = []
        # Only add same color cards if the last card is not a wild
        if lc[0] in ['r','g','b','y']:
            for rank in ['0','1','2','3','4','5','6','7','8','9','r','s','d']:
                legal_cards.append(lc[0] + rank)
        # Only add same rank cards if the last card has a valid rank
        if len(lc) > 1 and lc[1] in ['0','1','2','3','4','5','6','7','8','9','r','s','d']:
            for color in ['r','g','b','y']:
                legal_cards.append(color + lc[1])
        # Wild cards are always legal
        legal_cards.extend(['wi', 'w4'])
        return random.choice(legal_cards)
    i=0
    p_count = 0
    q=0
    rnd_count = random.randint(7,18)*4
    next_card = ""
    # Track consecutive none plays for each player
    player_none_counts = {player['name']: 0 for player in ordered_players}
    while win == False:
        while q+1<=rnd_count:
            p_count = len(ordered_players)
            if i+1 <= p_count:
                player = ordered_players[i]
                player_name = player['name']
                next_card = card_gen(table_card, player_none_counts[player_name])
                
                if next_card is None:
                    # Increment none count for this player
                    player_none_counts[player_name] += 1
                    # 33% chance of playing none again
                    if random.randint(1, 3) == 1:
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                    else:
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                    # Don't advance to next player - they go again
                else:
                    # Reset none count when playing a legal card
                    player_none_counts[player_name] = 0
                    print(f"{player['name']} plays",next_card)
                    print(next_card)
                    table_card = next_card
                    time.sleep(0.5)
                    # Only advance to next player when playing a legal card
                    i+=1
            else:
                i=0
            q+=1
        win = True
    u=0
    while u+1<=len(ordered_players):
        player = ordered_players[u]
        if player['name'] == "Colin":
            player_name = player['name']
            # Keep playing until they play a legal card
            while True:
                next_card = card_gen(table_card, player_none_counts[player_name])
                if next_card is None:
                    # Increment none count for this player
                    player_none_counts[player_name] += 1
                    # 33% chance of playing none again
                    if random.randint(1, 3) == 1:
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                    else:
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                    # Continue loop - they go again
                else:
                    # Reset none count when playing a legal card
                    player_none_counts[player_name] = 0
                    print(f"{player['name']} plays",next_card + "uno")
                    print(next_card+"uno")
                    table_card = next_card
                    time.sleep(0.5)
                    break  # Exit loop - they played a legal card
        else:
            player_name = player['name']
            # Keep playing until they play a legal card
            while True:
                next_card = card_gen(table_card, player_none_counts[player_name])
                if next_card is None:
                    # Increment none count for this player
                    player_none_counts[player_name] += 1
                    # 33% chance of playing none again
                    if random.randint(1, 3) == 1:
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                        print(f"{player['name']} plays None")
                        print("None")
                    else:
                        print(f"{player['name']} plays None")
                        print("None")
                        time.sleep(0.5)
                    # Continue loop - they go again
                else:
                    # Reset none count when playing a legal card
                    player_none_counts[player_name] = 0
                    print(f"{player['name']} plays",next_card)
                    print(next_card)
                    time.sleep(0.5)
                    break  # Exit loop - they played a legal card
            if next_card != None:
                table_card = next_card
        u+=1
    print("Remaining players:",[player['name'] for player in total_players])
    winner = ["Colin"]
    print("Winning players:",winner)
    os._exit(0)
