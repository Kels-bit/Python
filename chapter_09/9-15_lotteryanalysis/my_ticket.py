from random import choice

def player_ticket(number_pool):
    player_ticket = [] 
    plays = 0

    while plays <= 4:
        picks = choice(number_pool)
        if picks in player_ticket:    # Make winning ticket numbers unique(no duplicates)
            continue
        else:
            player_ticket.append(picks)
            plays += 1
    
    return player_ticket


