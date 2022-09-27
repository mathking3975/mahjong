import random

def shuffling():
    dummy = []
    for i in range(136):
        if i < 108:
            if 0 <= (i % 12) <= 3:
                dummy.append('p'+str(i//12+1))
            elif 4 <= (i % 12) <= 7:
                dummy.append('s'+str(i//12+1))
            else:
                dummy.append('m'+str(i//12+1))
        else:
            dummy.append('z'+str((i//4)-26))
    shuffled_deck = []
    for i in range(136):
        shuffled_deck.append(dummy.pop(random.randrange(0,136-i)))
    return shuffled_deck

def split_deck(Deck, p1, p2, p3, p4):
    dice = random.randrange(2,13)
    if dice % 4 == 1:
        place = dice*2
    elif dice % 4 == 2:
        place = dice*2+34
    elif dice % 4 == 3:
        place = dice*2+68
    else:
        place = dice*2+102
    for i in range(3):
        for j in range(4):
            for k in range(4):
                if j == 0: 
                    p1.append(Deck[place]) #pop을 쓰면 유국처리가 편함, 일반적으로 쓰면 place 숫자를 넘기기 편함
                elif j == 1:
                    p2.append(Deck[place])
                elif j == 2:
                    p3.append(Deck[place])
                else:
                    p4.append(Deck[place])
                place += 1
                if place == 136:
                    place = 0
    p1.append(Deck[place])
    place += 1
    p2.append(Deck[place])
    place += 1
    if place == 136:
        place = 0
    p3.append(Deck[place])
    place += 1
    p4.append(Deck[place])
    place += 1
    if place == 136:
        place = 0
    return Deck, p1, p2, p3, p4, place

Deck = []
p1 = []
p2 = []
p3 = []
p4 = []
place = 0
Deck, p1, p2, p3, p4, place = split_deck(shuffling(),p1,p2,p3,p4)
p1.sort()
p2.sort()
p3.sort()
p4.sort()
print(p1, p2, p3, p4, place)
