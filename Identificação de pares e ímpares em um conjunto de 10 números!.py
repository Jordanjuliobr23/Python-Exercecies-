print('Trabalhando com um conjunto de 10 números!')
x = 0
c= 0
qtdi=0
qtdp=0
soma1=0
soma2=0 
while c < 10: 
    n=int(input('Digite um número: ')) 
    if n % 2 == 0:
        par = True
        impar = False
        qtdp= qtdp + 1
    if n % 2 != 0: 
        impar = True
        par = False 
        qtdi= qtdi + 1 
    c= c + 1
    if par:
        soma1= soma1 + n
    if impar: 
        soma2= soma2 + n 
print(f'A soma dos PARES corresponde a: {soma1} ')
print(f'A soma dos IMPARES corresponde a: {soma2} ')
print(f'Existem {qtdp} números PARES')
print(f'Existem {qtdi} números IMPARES')

