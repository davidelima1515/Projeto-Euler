n, maximo, linha = 13, 13, 10 
# for de 13 até um milhão
for i in range(13, 10**6):
    #cada vez que o for inicia um novo loop a lista values é criada novamente.
    values = [i]
    while 1:
        #quando o valor chega a 1, o while para o numero é encerrado.     
        if i == 1:
            break
        elif i % 2 ==0:
            i = i/2
            values.append(i)
        else:
            i = 3*i + 1
            values.append(i)
    # se o numero de valores for maior que o valor de 13, então o novo valor toma conta.
    if len(values) >  linha:
        linha = len(values)
        maximo = n      
    # a cada novo numero é somado 1 a n para ajudar a achar o momento de maximo
    n += 1
print(maximo)