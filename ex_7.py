from especiais.primo import isprime

initial = 2
total = 0
while 1:
    if isprime(initial):
        total += 1
        if total == 10001:
            break
    initial += 1    

print(initial)