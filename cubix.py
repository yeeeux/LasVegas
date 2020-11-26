import random

def getDice():
    return random.randint(2,12)
def cubix(mon):
    playgame=True
    money=mon
    from mainmenu import message_in_stars
    from mainmenu import getInput
    from mainmenu import getIntInput
    from mainmenu import currency as valuta
    while playgame:
        print(f"У тебя на счету {money} {valuta}")
        stavka=getIntInput(0, money, f"Сделай ставку в пределах {money} {valuta}\n"
                    f"Введи 0, если хочешь слиться, дешёвка!\n"
                    f"")
        if stavka ==0:
            return money
        play = True
        stav = stavka
        oldResult = getDice()
        firstgame = True
        while play and stav >0 and money>0:
            if stavka>money:
                stavka=money
            print()
            print(f'\n В твоем распоряжении {stavka} {valuta}')
            print(f"\n Текущая сумма чисел на костях {oldResult}")
            print("\n Сумма чисел накостях будет больше, меньше или равна предыдущей?")

            x=getInput("0123","1 - больше (1: 1/5) , 2 - меньше (1: 1/5), 3 - равна (1: 3), 0 - выход")

            if x !="0":
                firstgame = False
                money-=stavka
                curresult = getDice()
                win=False
                if (oldResult > curresult):
                    if x == "2":
                        win=True
                elif(oldResult<curresult):
                    if (x=="1"):
                        win=True
                if not x =="3":
                    if win:
                        print(f"На столе выпала следующая сумма костей {curresult}")
                        message_in_stars("\033[32m Ты выиграл!!! \033[0m")
                        print(f"Твой выигрыш:\033[32m {stavka//5} {valuta} \033[0m")
                        money+=stavka+stavka//5
                        stavka+=stavka//5
                    else:
                        print(f"На столе выпала следующая сумма костей {curresult}")
                        message_in_stars("\033[31m Ты проиграл!!! \033[0m")
                        print(f"Ты проиграл:\033[31m {stavka} {valuta} \033[0m")
                        stavka=stav
                elif (x=="3"):
                    if (oldResult==curresult):
                        print(f"На столе выпала следующая сумма костей {curresult}")
                        message_in_stars("\033[32m Ты выиграл!!! \033[0m")
                        print(f"Твой выигрыш:\033[32m {stavka*2} {valuta} \033[0m")
                        money+=stavka*3
                        stavka*=3
                    else:
                        print(f"На столе выпала следующая сумма костей {curresult}")
                        message_in_stars("\033[31m Ты проиграл!!! \033[0m")
                        print(f"Ты проиграл:\033[31m {stavka} {valuta} \033[0m")
                        stavka = stav
                oldResult=curresult
            else:
                if firstgame:
                    money -=stavka
                play = False

