sum = 0
for num in range(1, 1001):
    sum += num**num

corte = str(sum)[-10:]
print(corte)