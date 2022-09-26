import random

def shuffling():
    dummy = []
    for i in range(136):
        if i < 108:
            if 0 <= (i % 12) <= 3:
                dummy.append(str(i//12+1)+'p')
            elif 4 <= (i % 12) <= 7:
                dummy.append(str(i//12+1)+'s')
            else:
                dummy.append(str(i//12+1)+'m')
        else:
            dummy.append(str((i//4)-26)+'z')
    shuffled_deck = []
    for i in range(136):
        shuffled_deck.append(dummy.pop(random.randrange(0,136-i)))
    return shuffled_deck

shuffling()