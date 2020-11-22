#константы
currency="RUB"
defaultMoney=10000
playGame=True

def getInput(digit, message):
    inputt=""
    while(inputt=="" or not inputt in digit):
        inputt=input(message)
    return (inputt)

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

message_in_stars("Во что поиграем сегодня?")
print("Ты можешь сыграть в:")
print("    ","1 - Рулетку")
print("    ","2 - Кости")
print("    ","3 - Слоты")
print("    ","0 - Выход")
getInput("0123","Введите число!")

# if int(choicegame()) == 0:
#     exitgame(loadmoney())


# message_in_stars("Приветствую тебя в нашем казино 'LASVEGAS'!")
# money=loadmoney()
# saveMoney(10000)
# startMoney=money
