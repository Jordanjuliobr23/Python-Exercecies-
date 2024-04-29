print('=-'*100)
print('Sistema de elevaodor: ')
n1=int(input('Por favor, digite o andar atual: '))
n2=int(input('Por favor, digite o andar de destino: '))
if n1 > n2:
    for c in range (n1,n2,-1):
        print(c)
    print(f'O elevador desceu até o andar número {n2}! ')
else: 
    for c in range (n1,n2):
        print(f'O elevador está no andar {c}')
    print(f'O elevador subiu até o andar número {n2}!')