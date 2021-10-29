import time
# numero para startar as verificações, se é divisível pelos 20 numeros do desafio (1 até 20).
initial = 19
inicio = time.time()
# estrutura de repetição que só vai ser parada se a minha condição for atingida.
while 1:
    # a função all devolve true se todos os numeros do meu range forem divisores do numero initial.
    if all([initial % number == 0 for number in range(1, 21)]):
        print(initial)
        print(time.time() - inicio)
        break
    # caso algum numero não seja divisor, meu else vai adicionar 19, pois o meu numero final tem que ser divisível por 19.
    # esse incremento poderia ser de 5, 10, 17 e etc.
    else:
        initial += 19
