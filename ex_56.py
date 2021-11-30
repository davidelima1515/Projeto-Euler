max = 0
for a in range(2, 100):
    for b in range(2, 100):
        total = 0
        n = a**b
        for i in str(n):
            total += int(i)
        if total > max:
            max = total

print(max)