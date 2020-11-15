#константы
currency="RUB"
defaultMoney=10000
playGame=True


def message_in_stars(message):
        print()
        print("*"*(len(message)+4))
        print(" ",message)
        print("*"*(len(message)+4))
def loadmoney:
    try:
        f=open("money.dat",'r')
        m=int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение по умолчанию: {defaultMoney} {currency}")
        m=defaultMoney
    return m
def saveMoney:
    try:
        f=open("money.dat", 'w')
        f.write(str(moneyTosave))
        f.close()
    except:
        print("Ошибка создания файла")
    quit(0)


message_in_stars("Приветствую тебя в нашем казино 'LASVEGAS'!")
money=loadmoney()
startMoney=money
