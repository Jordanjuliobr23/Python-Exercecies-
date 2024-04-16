print('=-'*100)
print('Leitura de números inteiros: Digite 999 para interromper a leitura')
n=0
soma=0
qtd=0
maior=0
menor= 100000000000000000
while n != 999: 
    n=int(input('Digite um número inteiro: '))
    soma= soma + n
    if n > maior: 
        maior= n
    if n < menor:
        menor= n  
    qtd= qtd + 1
    if n == 999: 
        break 
print(f'O maior número dos {qtd} digitados é o número {maior} ')
print(f'O menor número dos {qtd} digitados é o número {menor}') 
print(f'A soma dos {qtd} números digitados corresponde a {soma}')
