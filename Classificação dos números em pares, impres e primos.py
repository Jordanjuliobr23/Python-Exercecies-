print('=-'*100)
print('Classificação dos números: Par, Impar e Primo')
par=0
soma1=0
impar=0
soma2=0
primo=0
soma3=0 
for c in range (0,10):
    n=int(input('Digite um número: '))
    if n % 2 == 0: 
        par= par + 1
        soma1= soma1 + n 
    if n % 2 != 0: 
        impar= impar + 1 
        soma2= soma2 + n
    if n % 2 == 0 and n % n == 0: 
        par= par + 1
        soma1= soma1 + n 
        primo= primo + 1 
        soma3= soma3 + n
print('Analisando os números...')
print(f' Existem {par} pares, {impar} ímpares e {primo} primos!')
print(f'A soma entre os pares vale {soma1}')
print(f'A soma entre os ímpares vale {soma2}')
print(f'A soma entre os primos vale {primo}')