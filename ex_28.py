
initial, final, gap, rotacao = 1, 1001**2, 2, 0 
soma = 0
while initial < final:
    if rotacao == 0:
        soma += initial
    elif rotacao % 5== 0:
        gap += 2
    else:
        initial += gap 
        soma += initial
    rotacao += 1

print(soma)