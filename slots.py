from random import randint


result = []
slovar = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
result2 = []

def create_of_line():
    for i in range(5):
        result.append(randint(1, 9))
    return result

def create_of_windict():
    for i in result:
        for j in range(1,10):
            if i == j:
                slovar[j] += 1
    return slovar

def rate_of_win():
    for i in slovar.values():
        result2.append(i)
    return max(result2)

def counting_of_bet():
     if rate_of_win == 0:
         return bet * 0
     elif rate_of_win == 1:
         return bet * 0
     elif rate_of_win == 2:
         return bet * 1
     elif rate_of_win == 3:
         return bet * 1,2
     elif rate_of_win == 4:
         return bet * 1,5
     elif rate_of_win == 5:
         return bet * 2

















