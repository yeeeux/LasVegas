import random

def getInput(digit, message):
    inputt=""
    while(inputt=="" or not inputt in digit):
        inputt=input(message)
    return (inputt)
def getIntInput(min,max,mess):
    ret = -1
    while (ret<min or ret > max):
        st=input(mess)
        if st.isdigit():
            ret = int(st)
        else:
            print( "Введи целое число")
    return ret

def roulette():
    playGame = True
    playroulett = True
    money=10000
    valuta="RUB"
    while(playGame and money>0):
        print("ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
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
        if int(x)==0:
            return 0
        if playroulett:
            stavka = getIntInput(0, money, f"Сколько поставишь? (не больше {money})")
            if stavka == 0:
                return 0
            print()
            if int(x) == 1:
                print("Ты поставил на \033[31m красное ")
                if (number % 2 == 0):
                    print("На рулетке выпало Красное!")
                    money+=stavka
                    print(f"Твой выигрыш:{stavka} {valuta}")
                else:
                    print("На рулетке выпало черное(!")
                    money-=stavka
                    print(f"Твой проигрыш:{stavka} {valuta}")
            if int(x) == 2:
                print("Ты поставил на чёрное!")
                if (number %2 != 0):
                    print("На рулетке выпало Чёрное!")
                    money+=stavka
                    print(f"Твой выигрыш:{stavka} {valuta}")
                else:
                    print("На рулетке выпало Красное!")
                    money-=stavka
                    print(f"Твой проигрыш:{stavka} {valuta}")
            if int(x) == 3:
                print("Ты поставил на ЧЁТНОЕ!")
                if (number % 2 == 0):
                    print(f"На рулетке выпало {number}")
                    money+=stavka
                    print(f"Твой выигрыш:{stavka} {valuta}")
                else:
                    print(f"На рулетке выпало {number}")
                    money-=stavka
                    print(f"Твой проигрыш:{stavka} {valuta}")
            if int(x) == 4:
                print("Ты поставил на Нечётное!")
                if (number %2 != 0):
                    print(f"На рулетке выпало {number}")
                    money+=stavka
                    print(f"Твой выигрыш:{stavka} {valuta}")
                else:
                    print(f"На рулетке выпало {number}")
                    money-=stavka
                    print(f"Твой проигрыш:{stavka} {valuta}")
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
                    print(f"Твой выигрыш:{stavka*3} {valuta}")
                else:
                    money-=stavka
                    print(f"Твой проигрыш:{stavka} {valuta}")
            if int(x) == 6:
                print(f"Ты поставил на число: {chislo}")
                if (number == chislo):
                    print (f"На рулетке выпало число {number}")
                    money+=stavka*35
                    print(f"Твой выигрыш:{stavka*36} {valuta}")
                else:
                    print (f"На рулетке выпало число {number}")
                    money-=stavka
                    print(f"Твой проигрыш:{stavka} {valuta}")
            print()
            input("Нажмите ENTER для продолжения")




roulette()


