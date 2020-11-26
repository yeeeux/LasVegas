#константы
currency="RUB"
defaultMoney=10000
playGame=True
from roulett import roulette
from cubix import cubix
from slots import slots

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
            message_in_stars("Добро пожаловать в рулетку!")
            money=roulette(money)
        if x =="2":
            message_in_stars("Добро пожаловать в кости!")
            money=cubix(money)
        if x =="3":
            message_in_stars("Дергай за рычаг!")
            money=slots(money)
    if money <=0:
        print("Ты остался без денег! Срочно иди займи")
    if money> startMoney:
        print("Поздравляем с прибылью!!!")
        print(f"На начало игры у тебя было {startMoney} {currency}")
        print(f"Сейчас у тебя уже {money} {currency}, приходи играй еще в казино LASVEGAS")
    if money < startMoney:
        print(f"К сожалению ты проиграл {startMoney-money} {currency}")
        print(f"В следующий раз у тебя обязательно все получится!")
    saveMoney(money)

