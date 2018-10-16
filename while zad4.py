x = 1;
while x <= 10000000000:
    z = (x / 12)
    if int(z) != (x / 12):
        print("{}" .format(x))
    if int(z) == (x / 12):
        print("Trafilem na liczbe podzielna przez 12 jest to {}" .format(x))
        exit()
    x = x + 1
