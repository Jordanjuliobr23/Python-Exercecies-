print('=-'*100)
print('Soma de pares inteiros')
soma=0
for c in range (0,7):
    n=int(input('Digite um número: '))
    if n % 2: 
        soma= soma + n 
print(f'A soma dos números pares digitados corresponde a : {soma}')