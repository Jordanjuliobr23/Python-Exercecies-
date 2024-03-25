print('-='*100)
print('Este programa ler um ano digitado por um usuário e identifica se ele é ou não um ano bissexto')
n=int(input('Digite o ano desejado: '))
print('O ano digitado foi ', n)
if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
    print('Esse ano corresponde a um ano bissexto!')
else: 
    print('Esse ano NÃO corresponde a um ano bissexto!')
print('-='*100)
# 