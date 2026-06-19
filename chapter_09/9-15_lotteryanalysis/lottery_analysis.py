
def check_ticket(win_num, player_num):
    
    for winner in player_num:
        if winner not in win_num:
            return False

    return True


