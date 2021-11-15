from especiais.divisores import soma_divisores, isprime
soma = 0 
for num in range(1, 10000):
    a = soma_divisores(num)
    b = soma_divisores(a)
    if soma_divisores(a) == num and a != num:
        if not isprime(num) and not isprime(a):
            soma += num
            print(num, soma_divisores(num))
    

print(soma)