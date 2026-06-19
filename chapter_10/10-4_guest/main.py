from pathlib import Path

guest_name = input("what is your name? ")

path = Path('guest.txt')
path.write_text(guest_name)



