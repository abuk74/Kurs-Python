
print("podaj cyfre 1")
l1 = input()
print("podaj cyfre 2")
l2 = input()
print("podaj cyfre 3")
l3 = input()
print("podaj cyfre 4")
l4 = input()
print("podaj cyfre 5")
l5 = input()
print("podaj cyfre 6")
l6 = input()

def lotteryNo():
    import random
    integer = []
    for number in range(0 , 7):
        integer.append(random.randint(1, 49))
    return integer
print("Your numbuers are: {}, {}, {}, {}, {}, {}".format(l1, l2, l3, l4, l5, l6))
print ('Winning Numbers Are {}'. format(lotteryNo()))
print ('Thank You for playing')
