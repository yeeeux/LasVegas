from random import randint

def slots(mon):
    from mainmenu import getInput
    from mainmenu import getIntInput
    playGame = True
    money = mon
    valuta="RUB"
    result = []
    slovar = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    result2 = []
    while (playGame and money > 0):
        print("ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В СЛОТЫ!")
        print(f"У тебя на счету {money} {valuta}\n")
        print("Дергаем рычаг!!!")
        stavka = getIntInput(0, money, f"Сколько поставишь? (не больше {money})")
        print("Дергаем рычаг!!!")

        for i in range(5):
            result.append(randint(1, 9))
        print(result)

        for i in result:
            for j in range(1,10):
                if i == j:
                    slovar[j] += 1

        for i in slovar.values():
            result2.append(i)


        if max(result2) == 0:
            money -= stavka
            print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m")
        elif max(result2) == 1:
            money -= stavka
            print(f"Твой проигрыш:\033[31m {stavka} {valuta} \033[0m")
        elif max(result2) == 2:
            money = money
            print(f"Ты ничего не выйграл:\033[31m {stavka} {valuta} \033[0m")
        elif max(result2) == 3:
            money += stavka * 0,2
            print(f"Твой выигрыш составил: \033[32m {stavka} {valuta} \033[0m")
        elif max(result2) == 4:
            money += stavka * 0,5
            print(f"Твой выигрыш составил: \033[32m {stavka} {valuta} \033[0m")
        elif max(result2) == 5:
            money += stavka
            print(f"Твой выигрыш составил: \033[32m {stavka} {valuta} \033[0m")
        print()
        input("Нажмите ENTER для продолжения")

    return money













