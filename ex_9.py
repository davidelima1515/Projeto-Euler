for b in range(1000):
    for a in range(1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a*b*c)