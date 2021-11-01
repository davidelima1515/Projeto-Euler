from especiais.primo import isprime
number = 600851475143

for num in range(2, number):
    if number % num == 0 and isprime(num):
        print(num)