print('=-'*100)
print('Leitura de 10 números na ordem inversa!')
numeros=[]
for i in range (10):
    n=int(input(f'Digite o número {i+1}: '))
    numeros.append(n)
    numeros.reverse()
for n in numeros:
    print(n)