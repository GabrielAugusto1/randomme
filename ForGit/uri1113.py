x = 1
y = 10
    

while x!=y:
    x, y = map(int, input().split())

    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
