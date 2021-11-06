from especiais.primo import isprime
import time 

limit = 2*10**6
inicio = time.time()
soma = 2
for num in range(3, limit, 2):
    if isprime(num):
        print(num, soma)
        soma += num

print(soma)
print(time.time() - inicio)