#função recebe uma lista e calcula o produto dos itens dessa lista. 
def product(lista):
    p = 1
    for num in lista:
        p *= int(num)
    return p


