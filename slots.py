from random import randint



def slots(mon):
    from mainmenu import getIntInput
    from mainmenu import message_in_stars
    playGame = True
    money = mon
    valuta="RUB"
    message_in_stars("ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В СЛОТЫ!")
    print("2 цифры - возвращается ставка")
    print("3 цифры - (1:2)")
    print("4 цифры - (1:5)")
    print("5 цифр - (1:10)")
    while (playGame and money > 0):

        print(f"У тебя на счету {money} {valuta}\n")

        stavka = getIntInput(0, money, f"Сколько поставишь? (не больше {money}) \n"
                                       f"Введи 0, если хочешь слиться, дешёвка!\n"
                                       f"")
        if stavka == 0:
            playGame=False
            return money
        print("Дергаем рычаг!!!")

        result=[]
        result2=[]
        slovar = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

        for i in range(5):
            result.append(randint(1, 9))
        print(result)

        for i in result:
            for j in range(1,10):
                if i == j:
                    slovar[j] += 1

        for i in slovar.values():
            result2.append(i)

        if max(result2) == 1:
            money -= stavka
            print(f"Ты проиграл:\033[31m {stavka} {valuta} \033[0m")

        elif max(result2) == 2:
            money = money
            print(f"Ты ничего не выйграл, но и не проиграл! Тебе возвращается твоя ставка: \033[32m {stavka} {valuta} \033[0m")

        elif max(result2) == 3:
            if (((result[1]==result[2])and(result[2]==result[3])) or ((result[0]==result[1])and(result[1]==result[2]))or ((result[2]==result[3])and(result[3]==result[4]))):
                message_in_stars("ДЖЕК ПОТ!!!! Три цифры в ряд!!!")
                money += stavka * 3
                print(f"Твой выигрыш составил: \033[32m {stavka*3} {valuta} \033[0m")
            else:
                money += stavka * 2
                print(f"Твой выигрыш составил: \033[32m {stavka*2} {valuta} \033[0m")
        elif max(result2) == 4:
            if (((result[0]==result[1])and(result[1]==result[2])and(result[2]==result[3])) or ((result[1]==result[2])and(result[2]==result[3])and(result[3]==result[4]))):
                message_in_stars("ДЖЕК ПОТ!!!! Четыре цифры в ряд!!!")
                money += stavka * 7
                print(f"Твой выигрыш составил: \033[32m {stavka*7} {valuta} \033[0m")
            else:
                money += stavka * 5
                print(f"Твой выигрыш составил: \033[32m {stavka*5} {valuta} \033[0m")

        elif max(result2) == 5:
            if ((result[0]==7)):
                message_in_stars("HUUUUUUGE!!!! ДЖЕК ПОТ!!!! Пять топоров в ряд!!! Ты что крейзи???")
                money += stavka * 50
                print(f"Твой выигрыш составил: \033[32m {stavka*50} {valuta} \033[0m")
            else:
                money += stavka * 10
                print(f"Твой выигрыш составил: \033[32m {stavka*10} {valuta} \033[0m")

        print()
        input("Нажмите ENTER для продолжения\n"
              "")

    return money













