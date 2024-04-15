print('=-'*100)
print('Sistema de Progressão Aritmética')
n1=int(input('Digite o primeiro termo: '))
n2=int(input('Digite o último termo: '))
r=int(input('Digite a razão da PA: '))
for c in range (n1,n2+r,r):
    print(c,end=',')
