import random
import sys
import os

def iCanDoStep(last,arr):
    switch = False
    for i in arr:
        if last[0] == i[0] or last[1] == i[1]:
            switch = True
    return switch

        
player = [ ["7","♠"],["7","♦"],
           ["8","♥"],["8","♣"],
           ["9","♠"],["9","♦"],
           ["10","♣"],["10","♥"],
           ["J","♠"],["J","♦"],
           ["Q","♣"],["Q","♥"],
           ["K","♠"],["K","♦"],
           ["A","♣"],["A","♥"]]

computer = [ ["7","♥"],["7","♣"],
             ["8","♠"],["8","♦"],
             ["9","♥"],["9","♣"],
             ["10","♦"],["10","♠"],
             ["J","♥"],["J","♣"],
             ["Q","♣"],["Q","♦"],
             ["K","♥"],["K","♣"],
             ["A","♠"],["A","♦"]]


firstStep = random.choice([True,False])
print("Ваши карты :")

if firstStep:
    
    last = []
    
    print("За вами первый ход !")
    print("Ваши карты :")
    for i in player:
        print(i)
    print()
      
    while True:
        tmp = input("Выберите карту и масть (через пробел) :").split()
        if iCanDoStep(tmp,player):
            last = tmp
            player.remove(tmp)
            break

    while True:
        
        if len(player) == 0:
            print("У вас не осталось карт ! Вы выйграли !")
            sys.exit(0)

        if len(computer) == 0:
            print("У опонента не осталось карт ! Вы проиграли !")
            sys.exit(0)

        if iCanDoStep(last,computer):
            while True:
                step = random.choice(computer)
                if step[0] == last[0] or step[1] == last[1]:
                    last = step.copy()
                    computer.remove(step)
                    print("Опонент ложит карту :")
                    print(last)
                    break;
        else:
            print("Вы выйграли ! Опонент не может сделать ход !")
            print("Карты опонента :")
            print(computer)
            sys.exit(0)

        if iCanDoStep(last,player):
            print("Ваши карты :")
            for i in player:
                print(i)
            while True:
                tmp = input("Выберите карту и масть (через пробел) :").split()
                if iCanDoStep(tmp,player):
                    last = tmp
                    player.remove(tmp)
                    break
        else:
            print("Вы проиграли ! Вы не можете сделать ход !")
            print("Ваши карты :")
            print(player)
            sys.exit(0)
else:
    
    last = []

    print("Опонент ходит первый !")

    last = random.choice(computer)
    computer.remove(last.copy())
    print("Карта опонента : ")
    print(last)

    while True:

        if len(computer) == 0:
            print("У опонента не осталось карт ! Вы проиграли !")
            sys.exit(0)
        
        if len(player) == 0:
            print("У вас не осталось карт ! Вы выйграли !")
            sys.exit(0)
            
        if iCanDoStep(last,player):
            print("Ваши карты :")
            for i in player:
                print(i)
            while True:
                tmp = input("Выберите карту и масть (через пробел) :").split()
                if iCanDoStep(tmp,player):
                    last = tmp
                    player.remove(tmp)
                    break
        else:
            print("Вы проиграли ! Вы не можете сделать ход !")
            print("Ваши карты :")
            print(player)
            sys.exit(0)
            
        if iCanDoStep(last,computer):
            while True:
                step = random.choice(computer)
                if step[0] == last[0] or step[1] == last[1]:
                    last = step.copy()
                    computer.remove(step)
                    print("Опонент ложит карту :")
                    print(last)
                    break;
        else:
            print("Вы выйграли ! Опонент не может сделать ход !")
            print("Карты опонента :")
            print(computer)
            sys.exit(0)  
    
        
        
