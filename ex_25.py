a, b = 1, 1
index = 3
while 1:
    a, b = b, a + b
    index += 1
    if len(str(a+b))==1000:
        break
print(index)
