from random import randint


def lotto_machine():
    max_pool = 14
    numbers = 0
    character_pool = []

    while numbers <= max_pool:
        n = randint(1, 20)
        if n not in character_pool:   # Make the winnig pool number unique(no duplicates)
            character_pool.append(n)
            numbers += 1
        else:
            continue

    return character_pool
