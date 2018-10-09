print("podaj liczbe A")
a = int(input())
print("podaj liczbe B")
b = int(input())
z = (a / b)
if int(z) == a / b:
    print("{} jest podzielne przez {}".format(a, b))
else:
    print("{} nie jest podzielne przez {}".format(a, b))
