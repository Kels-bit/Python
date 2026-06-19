import lottery_machine,lottery_winticket,my_ticket,lottery_analysis


win = False
matches = 0

lotto_numbers = lottery_machine.lotto_machine()
winning_numbers = lottery_winticket.win_ticket(lotto_numbers)
player_numbers = my_ticket.player_ticket(lotto_numbers)


while not win:
    winning_numbers = lottery_winticket.win_ticket(lotto_numbers)
    win = lottery_analysis.check_ticket(winning_numbers, player_numbers)
    matches += 1

print(f"\nThe lottery number pool: {lotto_numbers}.")
print(f"Winning Ticket: {winning_numbers}.")
print(f"Player Ticket: {player_numbers}.")
print(f"Tries for a winning ticket: {matches}")



