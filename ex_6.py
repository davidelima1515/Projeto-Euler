def diferenca_total(number):
    soma_natural = sum([num for num in range(number + 1)])**2
    soma_quadrados = sum([num**2 for num in range(number + 1)])
    return soma_natural - soma_quadrados


print(diferenca_total(10))