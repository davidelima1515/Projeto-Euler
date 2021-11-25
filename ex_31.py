"""
    todas as situações em que uma única moeda é usada serão consideradas apenas no somatório total. 
"""
total = 8
#resolução por força bruta. 
for j in range(2):
    for k in range(4):
        for l in range(10):
            for m in range(20):
                for n in range(40):
                    for o in range(100):
                        for p in range(200):
                            if j*100 + k*50 + l*20 + m*10 + n*5 + o * 2 + p * 1 == 200:
                                total += 1

print(total)      