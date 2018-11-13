print("Podaj 5 liczb, oddziel je spacja")
yourTypes = input()


def lotteryNo():
    import random
    integer1 = []
    for number in range(0, 6):
        integer1.append(random.randint(1, 42))
    return integer1
integer1 = lotteryNo()

yourTypesList = list(map(int, yourTypes.split()))
c = set(yourTypesList) & set(integer1)
print("Trafiles " + str(len(c)) + " liczb")
print('Winning Numbers Are {}'.format(lotteryNo()))
print('Thank You for playing')
