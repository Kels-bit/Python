from random import choice

def win_ticket(number_pool):
    winning_ticket = [] 
    rolls = 0

    while rolls <= 4:
        picks = choice(number_pool)
        if picks in winning_ticket:    # Make winning ticket numbers unique(no duplicates)
            continue
        else:
            winning_ticket.append(picks)
            rolls += 1
    
    return winning_ticket


