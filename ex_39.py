#importando módulo que vai contar as quantidades de valores dentro de uma lista
from collections import Counter 
#lista que vai armazenar meus dados
valores = []
# como o perímetro máximo é 1000, então nosso a vai de 1 até 1000
for a in range(1, 1000):
    # como o perímetro máximo é 1000, tiramos "a" do range de b
    for b in range(1, 1000-a):
        # tirando "a" e "b" do range de C
        for c in range(1, 1000-a-b):
            if a**2 + b**2 == c**2:
                # adicionando o perímetro na nossa lista de valores. 
                valores.append(a+b+c)

#entrando com a lista no counter 
dados = Counter(valores)
#printando o valor mais comum dentro da nossa lista com sua moda. 
# obs: os valores da freq estão duplicados para todos os efeitos, caso seja necessário usar o valor, dividir por 2. 
print(dados.most_common(1)) 