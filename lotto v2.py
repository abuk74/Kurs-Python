print("Podaj 6 liczb, oddziel je spacja")
yourTypes = input()


def lotteryNo():
    import random
    integer1 = []
    for number in range(0, 7):
        integer1.append(random.randint(1, 49))
    return integer1
integer1 = lotteryNo()

yourTypesList = list(map(int, yourTypes.split()))
c = set(yourTypesList) & set(integer1)
print("Trafiles " + str(len(c)) + " liczb")
print('Winning Numbers Are {}'.format(lotteryNo()))
print('Thank You for playing')
