a, b = 1, 2
soma = 2 
limit = 4*10**6
while a + b < limit:
    a, b = b, a + b 
    if b % 2 == 0:
        soma +=b

print(soma)
