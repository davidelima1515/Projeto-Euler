def isprime(number):
    metade = int(number/2)
    if any([number % n ==0 for n in range(2, number)]):
        return False
    else:
        return True
