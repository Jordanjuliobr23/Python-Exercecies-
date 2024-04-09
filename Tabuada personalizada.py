print('=-'*100)
print('TABUADA PERSONALIZADA')
n=int(input('Digite um número para exibir sua tabuada personalizada: '))
i=int(input('Digite um número inteiro para iniciar a sua tabuada:  '))
f=int(input('Digite um número inteiro para encerrar sua tabuada: '))
qtd=0
s=0
print(f'Montar a tabuada de: {n}')
print(f'Começar por: {i}')
print(f'Irei exibir sua tabuada personalizada de {n}, começando de {i} e terminado {f}: ') 
while qtd < f:
    p= n * i
    print(f'{n} X {i} = {p}')
    i= i + 1 
    if i > f: 
        break 