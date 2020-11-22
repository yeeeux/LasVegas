#константы
currency="RUB"
defaultMoney=10000
playGame=True
from roulett import roulette

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

def message_in_stars(message):
        print()
        print("*"*(len(message)+4))
        print(" ",message)
        print("*"*(len(message)+4))
def loadmoney():
    try:
        f=open("money.dat",'r')
        m=int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение по умолчанию: {defaultMoney} {currency}")
        m=defaultMoney
    return m
def saveMoney(moneytoSave):
    try:
        f=open("money.dat", 'w')
        f.write(str(moneytoSave))
        f.close()
    except:
        print("Ошибка создания файла")
    quit(0)

def exitgame(m):
    print(f'Жаль что ты уходишь. Возвращайся завтра. Твой баланс {m}')


def main():
    playGame = True
    money=loadmoney()
    startMoney=money
    while (playGame and money>0):
        print("Приветствую тебя в нашем казино, Дружище!")
        message_in_stars("Во что поиграем сегодня?")
        print(f"У тебя на счету {money}")
        print("Ты можешь сыграть в:")
        print("    ","1 - Рулетку")
        print("    ","2 - Кости")
        print("    ","3 - Слоты")
        print("    ","0 - Выход")
        x = getInput("0123","Введите число!")
        if x == "0":
            playGame=False
            exitgame(money)
        if x =="1":
            # roulette(money)
            money=roulette(money)



