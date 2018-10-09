print("podaj dlugosc boku AB")
AB = float(input())
print("podaj dlugosc boku AC")
AC = float(input())
print("podaj dlugosc boku BC")
BC = float(input())
a = AB
b = BC
c = AC
z = (a**2 + b**2)
c2 = (c**2)
if z == c2:
    print("prostokatny")
else:
    print("nie jest prostokatny")
