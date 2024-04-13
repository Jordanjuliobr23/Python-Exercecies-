print('=-'*100)
print('Sistema de controle de acesso em uma portaria')
n=str(input('Digite seu nome: '))
i=int(input('Digite sua idade: '))
if i < 18: 
    print(f'Acesso negado para menores de 18 anos, por favor ligue para o morador vir buscá-lo na portaria pessoalmente!')
if i >= 18: 
    a=str(input('Possui autorização para entrar no condomínio: ')) 
    if a == 'sim':
        print('Acesso permitiido ao condomínio, seja bem-vindo!')
    if a == 'não':
        print('Por não possuir autorização para ingressar ao condomínio seu acesso NÃO será permitido ao condomínio!')
    