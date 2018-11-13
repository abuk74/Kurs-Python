print("Podaj 10 liczb, oddziel je spacja")
yourTypes = input()


def lotteryNo():
    import random
    integer1 = []
    for number in range(0, 21):
        integer1.append(random.randint(1, 80))
    return integer1
integer1 = lotteryNo()

yourTypesList = list(map(int, yourTypes.split()))
c = set(yourTypesList) & set(integer1)
print("Trafiles " + str(len(c)) + " liczb")
print('Winning Numbers Are {}'.format(lotteryNo()))
print('Thank You for playing')
