from especiais.fatorial import fatorial
total = 0
for n in range(1, 101):
    for r in range(n-1):
        combinacao = fatorial(n)/(fatorial(r)*fatorial(n-r))
        if combinacao > 10**6:
            total += 1
print(total)
