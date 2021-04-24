a = 0
g = 0 
d = 0
x = int(input())
while x != 4:
  if x==1:
    a += 1
  if x==2:
    g+=1
  if x==3:
    d+=1
  x = int(input())
  if x>4 or x<=0:
    x = int(input())

print('MUITO OBRIGADO')
print('Alcool: %d'%a)
print('Gasolina: %d'%g)
print('Diesel: %d'%d)
