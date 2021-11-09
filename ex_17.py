from especiais.list_1_to_1000 import numbers

soma = 0
for i in numbers:
    valor = numbers.get(i)
    if len(valor.split(" ")) == 1:
        if "-" in valor:
            print(valor, len(valor)-1)
            soma += len(valor)-1
        else:
            print(valor, len(valor))
            soma += len(valor)
    elif i % 10 == 0:
        if i % 100 == 0:
            print(valor, len(valor)-1)
            soma += len(valor) -1
        else:
            print(valor, len(valor) - len(valor.split(" ")) +4)
            soma += len(valor)-len(valor.split(" ")) + 4
    else:
        if "-" in valor:
            print(valor, len(valor)-len(valor.split(" ")) + 3 )
            soma += len(valor)-len(valor.split(" ")) + 3
        else:
            print(valor, len(valor)-len(valor.split(" ")) + 4 )
            soma += len(valor)-len(valor.split(" ")) + 4
print(soma)