a = int(input())
b = int(input())

soma = 0

if a>b:
    for i in range(b, a+1):
        if i%13!=0:
            soma+=i
if b>a:
    for i in range(a, b+1):
        if i%13!=0:
            soma+=i

print(soma)
