import random

def roulette(mon):
    from mainmenu import getInput
    from mainmenu import getIntInput
    from mainmenu import currency as valuta
    playGame = True
    money = mon
    while(playGame and money>0):
        print(f"У тебя на счету {money} {valuta}\n")
        print("Ставлю на...")
        print("1 - КРАСНОЕ!(выигрыш 1:1)")
        print("2 - ЧЁРНОЕ!(выигрыш 1:1)")
        print("3 - ЧЁТНОЕ!(выигрыш 1:1)")
        print("4 - НЕЧЁТНОЕ!(выигрыш 1:1)")
        print("5 - ДЮЖИНА!(выигрыш 3:1)")
        print("6 - МНЕ везет! Ставлю на число...")
        print("0 - Нужно отдохнуть. Вернуться в предыдущее меню")

        x=getInput("0123456","Твой выбор")
        number= random.randint(0,36)
        playroulett=True

        if int(x)==5:
            print()
            print("Выбери диапазон чисел:")
            print("1 - От 1 до 12")
            print("2 - От 13 до 24")
            print("3 - От 25 до 36")
            print("0 - Назад")
            duzhina=getInput("0123", "Твой выбор?")
            if (duzhina == "1"):
                textDuzhina="От 1 до 12"
            if (duzhina == "2"):
                textDuzhina="От 13 до 24"
            if (duzhina == "3"):
                textDuzhina="От 25 до 36"
            if (duzhina == "0"):
                playroulett=False
        if x=="6":
            chislo=getIntInput(0,36, "На какое число ставишь?(0-36):")
        if int(x)==0 or money==0:
            return int(money)
        if playroulett:
            stavka = getIntInput(0, money, f"Сколько поставишь? (не больше {money})")
            if stavka == 0:
                return 0
            print()
            if int(x) == 1:
                print("Ты поставил на \033[31m красное \033[0m ")
                if (number % 2 == 0):
                    print("На рулетке выпало \033[31m Красное!\033[0m")
                    money+=stavka
                    print(f"Твой выигрыш составил: \033[32m {stavka} {valuta} \033[0m")
                else:
                    print("На рулетке выпало \033[30m черное(! \033[0m")
                    money-=stavka
                    print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m ")
            if int(x) == 2:
                print("Ты поставил на \033[30m чёрное!  \033[0m")
                if (number %2 != 0):
                    print("На рулетке выпало \033[30m чёрное!  \033[0m")
                    money+=stavka
                    print(f"Твой выигрыш:\033[32m {stavka} {valuta} \033[0m")
                else:
                    print("На рулетке выпало  \033[31m Красное!\033[0m")
                    money-=stavka
                    print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m")
            if int(x) == 3:
                print("Ты поставил на ЧЁТНОЕ!")
                if (number % 2 == 0):
                    print(f"На рулетке выпало {number}")
                    money+=stavka
                    print(f"Твой выигрыш:\033[32m {stavka} {valuta} \033[0m")
                else:
                    print(f"На рулетке выпало {number}")
                    money-=stavka
                    print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m")
            if int(x) == 4:
                print("Ты поставил на Нечётное!")
                if (number %2 != 0):
                    print(f"На рулетке выпало {number}")
                    money+=stavka
                    print(f"Твой выигрыш:\033[32m {stavka} {valuta} \033[0m")
                else:
                    print(f"На рулетке выпало {number}")
                    money-=stavka
                    print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m")
            if int(x) == 5:
                print(f"Ты поставил на диапазон: {textDuzhina}")
                winduzhina=""
                if (number>-1 and number<13):
                    winduzhina="1"
                if (number>12 and number<25):
                    winduzhina="2"
                if (number>24 and number<37):
                    winduzhina="3"
                print (f"На рулетке выпало число {number}")
                if duzhina==winduzhina:
                    money+=stavka*2
                    print(f"Твой выигрыш:\033[32m {stavka*3} {valuta} \033[0m")
                else:
                    money-=stavka
                    print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m")
            if int(x) == 6:
                print(f"Ты поставил на число: {chislo}")
                if (number == chislo):
                    print (f"На рулетке выпало число {number}")
                    money+=stavka*35
                    print(f"Твой выигрыш::\033[32m {stavka*36} {valuta} \033[0m")
                else:
                    print (f"На рулетке выпало число {number}")
                    money-=stavka
                    print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m")
            print()
            input("Нажмите ENTER для продолжения")
    return money

