print('=-'*100)
print('Sistema de Progressão Aritmética usando While')
n1=int(input('Digite o primeiro termo: '))
nf=int(input('Digite o último termo: '))
r=int(input('Digte a razão da PA: '))
c= 0
t= 1
while c < nf: 
    print(f'O termo {t} da progressão aritmética é {n1}')
    t= t + 1
    n1= n1 + r 
    if c == nf:
        print(f'O último termo da progressão aritmética é {nf}')
    c= c + r