from especiais.fatorial import fatorial

total = 0
for i in range(3, 99999):
    soma = 0 
    for v in str(i):
        soma += fatorial(int(v))
    if soma == i:
        total += soma
print(total)