conjunto = set()
for a in range(2, 101):
    for b in range(2, 101):
        conjunto.add(a**b)

print(len(conjunto))
