print('=-'*100)
print('Coleção de CDS')
qtd=int(input('Digite a quantidade de CDS presentes na coleção: '))
n=0
soma=0
while n < qtd:
    p=float(input('Por favor, digite o preço referente ao CD: R$'))
    soma= soma + p 
    n= n + 1
    media= soma/qtd
print('=-'*100)
print(f'A quantidade de CDS da coleção do usuário corresponde a {qtd}')
print(f'A média de preços dos {qtd} CDS da coleção correponde a R${media}')