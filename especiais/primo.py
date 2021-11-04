def isprime(number):
    if number == 1:
        return False
    elif number % 2 == 0:
        if number == 2:
            return True
        else:
            return False
    elif number < 100000:
        if number == 3 or number == 5 or number == 7:
            return True    
        elif number % 3 == 0 or number % 5== 0 or number % 7==0:
            return False
        elif any([number % n == 0 for n in range(3, int(number/3))]):
            return False
        else:
            return True
    else:
        if number % 3 == 0 or number % 5== 0 or number % 7==0:
            return False
        elif any([number % n == 0 for n in range(3, int(number/100))]):
            return False
        else:
            return True










