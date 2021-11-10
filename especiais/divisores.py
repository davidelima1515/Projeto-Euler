
from especiais.primo import isprime

def soma_divisores(number):
    if number == 1:
        return 1
    if isprime(number):
        return (1 + number)
    elif  number % 2 == 0:
        divisores = [num for num in range(1, int(number/2 + 1)) if number % num == 0]
        return sum(divisores) 
    else:
        divisores = [num for num in range(1, int(number/primeiro_divisor(number) +1)) if number % num == 0]
        return sum(divisores) 



def primeiro_divisor(number):
    num = 3
    while 1:
        if number % num == 0:
            return num
            break
        else: 
            num += 2
