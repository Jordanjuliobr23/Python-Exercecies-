print('=-'*100)
print('Leitura de notas usando lista')
notas=[]
qtd=int(input('Por favor, digite a quantidade de notas: '))
soma=0
i=0
for i in range (qtd): 
    n=float(input(f'Por favor digite a nota {i+1}: ')) 
    notas.append(n)
    soma= soma + n
    media= soma//qtd 
print(f'As {qtd} notas apresentas são: ')
print(notas)
print(f'A média dessas notas correspondem a: {media}')