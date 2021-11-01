
def numero_divisores(number):
    divisores = [num for num in range(1, int(number/2)) if number % num == 0]
    if number == 3 :
        return 2
    if number % 2 == 0:
            return len(divisores) + 2 
            
    else:
        return len(divisores) + 1
