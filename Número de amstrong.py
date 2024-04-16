print('=-'*100)
print('Identificando um número de Amstrong a partir da análise de um número inteiro!')
n=int(input('Digite um número inteiro: '))
qtd=0 
soma= 0 
temp= n 
while temp > 0: 
    # encontrar quantos digitos existem na variável n (quantidade de digitos)
    temp= temp // 10 
    qtd= qtd + 1
temp=n 
while temp > 0: 
    # encontrar o digito (posição de cada digito)
    digito= temp % 10 
    # digito elevado a quantidade de digitos
    potencia=  digito ** qtd 
    soma= soma + potencia 
    temp= temp // 10
if soma == n: 
    print(f'O número {n} é um número de Amstrong!')
else:
    print(f'O número {n} NÃO é um número de Amstrong!')