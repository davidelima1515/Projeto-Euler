
# importando pacote para avaliar se numero é primo
from especiais.primo import isprime

# criando lista de numeros até um numero que com toda certeza supera 50 milhões quando elevado ao quadrado
lista_primos = [num for num in range(2, 7100) if isprime(num)]
#definindo um conjunto, que guarda numeros únicos 
soma = set()
# como o primeiro numero nós vamos elevar a 4 potência, ele pode assumir valores bem baixos para não superar 50 milhões 
for j in lista_primos:
    if j < 100:
        for k in lista_primos:
            # esse vai ser elevado a 3 potencia, então pode assumir numeros de grandeza inferior a 400
            if k < 400:
                for l in lista_primos:
                    # como a lista foi pensada nos primos até o máximo elevado a 2, então não precisa condicionar isso
                    # foi criada uma variável com a soma dos valores elevados de forma a facilitar a entrega. 
                    total = j ** 4 + k ** 3 + l **2
                    if  total <= 50*10**6:
                        # caso o numero total seja inferior a 50 milhões ele é adicionado ao set.
                        soma.add(total)

# finalmente, é feita a impressão do tamanho do nosso set. 
print(len(soma))
