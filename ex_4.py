maximo = 0
#range de 100 até mil, pois inclui 100 e finaliza em 999. Dessa forma, pega todos os numeros com 3 digitos.
for i in range(100, 1000):   
    for n in range(100, 1000):
        # transformando em string para facilitar na hora de pegar o inverso.
        transformada = str(i * n)  
        if transformada == transformada[::-1]:
            # como o desafio pede o numero máximo formado, esse código vai filtrar e pegar o máximo.
            if i*n > maximo: 
                maximo = i* n

print(maximo)