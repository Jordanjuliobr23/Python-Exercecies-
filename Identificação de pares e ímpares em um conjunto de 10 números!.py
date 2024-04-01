print('Trabalhando com um conjunto de 10 números!')
c= 0
soma1=0
soma2=0 
while c < 10: 
    n=int(input('Digite um número: ')) 
    if n % 2 == 0:
        par = True
        impar = False
        c= c + 1
    if n % 2 != 0: 
        impar = True
        par = False 
        c= c + 1
    if par:
        soma1= soma1 + n
    if impar: 
        soma2= soma2 + n 
print(f'Existem {soma1} números PARES')
print(f'Existem {soma2} números IMPARES')

