print('=-'*100)
print('Leitura de um vetor de 5 números inteiros!')
vetor=[]
for i  in range (5): 
    numero=int(input(f'Digite o número {i+1}: '))
    vetor.append(numero)
print('Os números inseridos pelo usuário foram: ')
for numero in vetor: 
    print(vetor)