number = ""
for i in range(0, 200000):
    number += str(i)

expression = int(number[1])*int(number[10]) * int(number[100]) * int(number[1000]) * int(number[10000]) * int(number[100000]) * int(number[1000000])

print(expression)